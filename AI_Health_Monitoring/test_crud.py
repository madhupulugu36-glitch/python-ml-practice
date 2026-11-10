
from crud import save_medical_record, get_all_medical_records

sample_record = {
    "Test Name": "Hemoglobin",
    "Value": 14.0,
    "Unit": "g/dL",
    "Patient Age (years)": 29,
    "Test Date": "2026-10-15",
    "Source": "Manual entry",
}

record_id = save_medical_record(sample_record)

print("Record saved successfully!")
print("Generated ID:", record_id)

records = get_all_medical_records()

print("Total saved records:", len(records))
print("Latest record:", records[0])