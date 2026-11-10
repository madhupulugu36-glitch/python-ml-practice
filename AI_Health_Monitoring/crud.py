
from datetime import date

from sqlalchemy.orm import Session

from db_connection import engine
from models import MedicalRecord
from patient_crud import Patient


def save_medical_record(record):
    """Save one medical measurement for a registered patient."""

    patient_id = int(record["Patient ID"])

    with Session(engine) as session:
        patient = session.get(Patient, patient_id)

        if patient is None:
            raise ValueError(
                f"Patient ID {patient_id} does not exist."
            )

        medical_record = MedicalRecord(
            patient_id=patient_id,
            test_name=record["Test Name"],
            value=float(record["Value"]),
            unit=record["Unit"],
            patient_age=int(record["Patient Age (years)"]),
            test_date=date.fromisoformat(
                str(record["Test Date"])[:10]
            ),
            source=record["Source"],
        )

        session.add(medical_record)
        session.commit()
        session.refresh(medical_record)

        return medical_record.id


def save_medical_records(records):
    """Save multiple measurements for registered patients."""

    saved_ids = []

    with Session(engine) as session:
        try:
            for record in records:
                patient_id = int(record["Patient ID"])
                patient = session.get(Patient, patient_id)

                if patient is None:
                    raise ValueError(
                        f"Patient ID {patient_id} does not exist."
                    )

                medical_record = MedicalRecord(
                    patient_id=patient_id,
                    test_name=record["Test Name"],
                    value=float(record["Value"]),
                    unit=record["Unit"],
                    patient_age=int(
                        record["Patient Age (years)"]
                    ),
                    test_date=date.fromisoformat(
                        str(record["Test Date"])[:10]
                    ),
                    source=record["Source"],
                )

                session.add(medical_record)
                session.flush()

                saved_ids.append(medical_record.id)

            session.commit()
            return saved_ids

        except Exception:
            session.rollback()
            raise


def get_all_medical_records():
    """Retrieve all medical measurements."""

    with Session(engine) as session:
        records = (
            session.query(MedicalRecord)
            .order_by(MedicalRecord.id.desc())
            .all()
        )

        return [
            {
                "ID": record.id,
                "Patient ID": record.patient_id,
                "Test Name": record.test_name,
                "Value": record.value,
                "Unit": record.unit,
                "Patient Age (years)": record.patient_age,
                "Test Date": record.test_date.isoformat(),
                "Source": record.source,
            }
            for record in records
        ]


def get_medical_records_by_patient(patient_id):
    """Retrieve medical measurements for one patient only."""

    with Session(engine) as session:
        patient = session.get(Patient, int(patient_id))

        if patient is None:
            raise ValueError(
                f"Patient ID {patient_id} does not exist."
            )

        records = (
            session.query(MedicalRecord)
            .filter(MedicalRecord.patient_id == patient.patient_id)
            .order_by(MedicalRecord.test_date.desc())
            .all()
        )

        return [
            {
                "ID": record.id,
                "Patient ID": record.patient_id,
                "Test Name": record.test_name,
                "Value": record.value,
                "Unit": record.unit,
                "Patient Age (years)": record.patient_age,
                "Test Date": record.test_date.isoformat(),
                "Source": record.source,
            }
            for record in records
        ]


def delete_medical_record(record_id):
    """Delete one medical measurement by its ID."""

    with Session(engine) as session:
        record = session.get(MedicalRecord, record_id)

        if record is None:
            return False

        session.delete(record)
        session.commit()

        return True