
import hashlib
from datetime import date

import pandas as pd
import streamlit as st

from crud import (
    save_medical_record,
    save_medical_records,
    get_all_medical_records,
)
from patient_crud import get_all_patients


st.set_page_config(
    page_title="AI Health Monitoring",
    page_icon="🏥",
    layout="wide",
)

st.title("🏥 AI Health Monitoring System")
st.write(
    "Enter medical measurements or upload a report. "
    "Every new measurement must belong to a registered patient."
)


# -----------------------------
# Load Registered Patients
# -----------------------------
try:
    patients = get_all_patients()
except Exception:
    st.error("Unable to load registered patients from MySQL.")
    st.stop()


patient_lookup = {
    patient["Patient ID"]: patient
    for patient in patients
}

patient_ids = list(patient_lookup.keys())


# -----------------------------
# Patient Selection
# -----------------------------
st.header("1. Select Patient")

selected_patient_id = None

if patients:
    selected_patient_id = st.selectbox(
        "Choose the patient for this medical report or entry",
        options=patient_ids,
        format_func=lambda pid: (
            f'{patient_lookup[pid]["Patient Code"]} - '
            f'{patient_lookup[pid]["Patient Name"]}'
        ),
        key="selected_patient_id",
    )

    selected_patient = patient_lookup[selected_patient_id]

    st.info(
        f'Patient: {selected_patient["Patient Name"]} | '
        f'Code: {selected_patient["Patient Code"]} | '
        f'Age status: {selected_patient["Age Status"]}'
    )

    if selected_patient["Age Status"] == "approximate":
        if selected_patient.get("Birth Year"):
            approximate_age = (
                date.today().year - selected_patient["Birth Year"]
            )
            st.caption(
                f"Approximate age: {approximate_age} years. "
                "Birth year alone cannot establish exact age."
            )
        else:
            st.caption(
                "The patient's age is approximate. "
                "Confirm age information before clinical interpretation."
            )

else:
    st.warning(
        "No patients are registered yet. Register a patient "
        "before saving medical measurements."
    )


# -----------------------------
# Measurement Details
# -----------------------------
st.header("2. Measurement Details")

col1, col2 = st.columns(2)

with col1:
    patient_age = st.number_input(
        "Patient age at the time of testing (years)",
        min_value=0,
        max_value=120,
        value=29,
        step=1,
        help=(
            "Enter the patient's age at the test date. "
            "This is stored as a historical age snapshot."
        ),
    )

with col2:
    test_date = st.date_input(
        "Test date",
        value=date.today(),
    )


# -----------------------------
# Upload CSV or Excel
# -----------------------------
st.header("3. Upload Medical Report")

uploaded_file = st.file_uploader(
    "Upload a CSV or Excel file",
    type=["csv", "xlsx"],
    key="medical_report_upload",
)

if uploaded_file is not None:
    try:
        file_bytes = uploaded_file.getvalue()
        file_hash = hashlib.sha256(file_bytes).hexdigest()

        if uploaded_file.name.lower().endswith(".csv"):
            uploaded_df = pd.read_csv(uploaded_file)
        else:
            uploaded_df = pd.read_excel(uploaded_file)

        required_columns = ["Test Name", "Value", "Unit"]

        missing_columns = [
            column
            for column in required_columns
            if column not in uploaded_df.columns
        ]

        if missing_columns:
            st.error(
                "Missing required columns: "
                + ", ".join(missing_columns)
            )

        elif uploaded_df.empty:
            st.warning("The uploaded report contains no records.")

        else:
            uploaded_df = uploaded_df[required_columns].copy()

            uploaded_df["Test Name"] = (
                uploaded_df["Test Name"]
                .astype("string")
                .str.strip()
            )

            uploaded_df["Unit"] = (
                uploaded_df["Unit"]
                .astype("string")
                .str.strip()
            )

            uploaded_df["Value"] = pd.to_numeric(
                uploaded_df["Value"],
                errors="coerce",
            )

            invalid_rows = (
                uploaded_df["Test Name"].isna()
                | uploaded_df["Test Name"].eq("")
                | uploaded_df["Unit"].isna()
                | uploaded_df["Unit"].eq("")
                | uploaded_df["Value"].isna()
                | ~uploaded_df["Value"].map(
                    lambda value: (
                        pd.notna(value)
                        and abs(value) != float("inf")
                    )
                )
            )

            if invalid_rows.any():
                st.error(
                    "Some rows contain missing names, missing units, "
                    "or invalid numeric values. Please correct the file."
                )

                st.dataframe(
                    uploaded_df[invalid_rows],
                    use_container_width=True,
                )

            else:
                st.subheader("Uploaded Report Preview")
                st.dataframe(
                    uploaded_df,
                    use_container_width=True,
                )

                upload_button_key = f"imported_report_{file_hash}"

                if upload_button_key not in st.session_state:
                    st.session_state[upload_button_key] = False

                if st.button(
                    "Save Uploaded Values to MySQL",
                    key=f"save_upload_{file_hash}",
                    disabled=selected_patient_id is None,
                ):
                    if st.session_state[upload_button_key]:
                        st.info(
                            "This file has already been imported "
                            "in this dashboard session."
                        )

                    else:
                        records = []

                        for _, row in uploaded_df.iterrows():
                            records.append(
                                {
                                    "Patient ID": selected_patient_id,
                                    "Test Name": str(row["Test Name"]),
                                    "Value": float(row["Value"]),
                                    "Unit": str(row["Unit"]),
                                    "Patient Age (years)": int(
                                        patient_age
                                    ),
                                    "Test Date": test_date.isoformat(),
                                    "Source": uploaded_file.name,
                                }
                            )

                        try:
                            saved_ids = save_medical_records(records)

                            st.session_state[
                                upload_button_key
                            ] = True

                            st.success(
                                f"Saved {len(saved_ids)} measurements "
                                f"for patient ID {selected_patient_id}."
                            )

                            st.rerun()

                        except Exception:
                            st.error(
                                "Unable to save the uploaded report. "
                                "No measurements from this batch should "
                                "be considered saved unless the transaction "
                                "committed successfully."
                            )

                            st.exception(Exception(
                                "Check the terminal for the full error."
                            ))

    except Exception as error:
        st.error("Unable to read or process the uploaded file.")
        st.exception(error)


# -----------------------------
# Manual Medical Entry
# -----------------------------
st.header("4. Add a Medical Measurement")

with st.form("manual_medical_entry", clear_on_submit=True):
    test_name = st.text_input(
        "Test name",
        placeholder="Example: Hemoglobin",
    )

    value = st.number_input(
        "Measurement value",
        value=0.0,
        format="%.4f",
    )

    unit = st.text_input(
        "Unit",
        placeholder="Example: g/dL",
    )

    manual_submit = st.form_submit_button(
        "Save Manual Entry to MySQL",
        disabled=selected_patient_id is None,
    )


if manual_submit:
    if not test_name.strip() or not unit.strip():
        st.error("Please enter both the test name and unit.")

    else:
        record = {
            "Patient ID": selected_patient_id,
            "Test Name": test_name.strip(),
            "Value": value,
            "Unit": unit.strip(),
            "Patient Age (years)": int(patient_age),
            "Test Date": test_date.isoformat(),
            "Source": "Manual entry",
        }

        try:
            record_id = save_medical_record(record)

            st.success(
                f"Measurement saved! Record ID: {record_id}"
            )

            st.rerun()

        except Exception as error:
            st.error("Unable to save the measurement.")
            st.exception(error)


# -----------------------------
# Display and Filter Records
# -----------------------------
st.header("5. Saved Medical Records")

try:
    records = get_all_medical_records()

    if records:
        records_df = pd.DataFrame(records)

        st.metric(
            "Total saved measurements",
            len(records_df),
        )

        filter_options = ["All patients"] + patient_ids

        selected_filter = st.selectbox(
            "Filter records by patient",
            options=filter_options,
            format_func=lambda pid: (
                "All patients"
                if pid == "All patients"
                else (
                    f'{patient_lookup[pid]["Patient Code"]} - '
                    f'{patient_lookup[pid]["Patient Name"]}'
                )
            ),
        )

        if selected_filter != "All patients":
            records_df = records_df[
                records_df["Patient ID"] == selected_filter
            ]

        st.dataframe(
            records_df,
            use_container_width=True,
            hide_index=True,
        )

        csv_data = records_df.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            "Download Displayed Records as CSV",
            data=csv_data,
            file_name="medical_records.csv",
            mime="text/csv",
        )

    else:
        st.info("No medical measurements have been saved yet.")

except Exception as error:
    st.error("Unable to retrieve records from MySQL.")
    st.exception(error)


st.caption(
    "Educational project only. Displayed values are not diagnoses. "
    "Verify patient identity, units, and clinical reference ranges "
    "before interpreting any medical measurements."
)