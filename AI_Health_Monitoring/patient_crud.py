
from datetime import date

from sqlalchemy import (
    Column,
    Integer,
    SmallInteger,
    String,
    TIMESTAMP,
    select,
    text,
)
from sqlalchemy.orm import Session, relationship
from models import Base

from db_connection import engine


PatientBase = Base


class Patient(PatientBase):
    __tablename__ = "patients"

    patient_id = Column(Integer, primary_key=True, autoincrement=True)
    patient_code = Column(String(20), unique=True, nullable=False)
    patient_name = Column(String(150), nullable=False)

    medical_records = relationship(
    "MedicalRecord",
    back_populates="patient",
)

    birth_year = Column(SmallInteger, nullable=True)
    age_group = Column(String(30), nullable=True)
    age_status = Column(
        String(20),
        nullable=False,
        server_default=text("'unknown'"),
    )

    gender = Column(String(30), nullable=True)
    phone = Column(String(20), nullable=True)

    created_at = Column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
    )


def register_patient(
    patient_name,
    birth_year=None,
    age_group=None,
    age_status="unknown",
    gender=None,
    phone=None,
):
    """Register a patient and return their generated patient details."""

    patient_name = patient_name.strip()

    if not patient_name:
        raise ValueError("Patient name is required.")

    current_year = date.today().year

    if birth_year is not None:
        birth_year = int(birth_year)

        if not 1900 <= birth_year <= current_year:
            raise ValueError(
                f"Birth year must be between 1900 and {current_year}."
            )

        # Birth year gives an approximate age, not an exact age.
        age_status = "approximate"
        age_group = None

    elif age_status == "approximate":
        if not age_group or not age_group.strip():
            raise ValueError(
                "Provide an approximate age group when birth year is unknown."
            )

    elif age_status == "unknown":
        age_group = None

    else:
        raise ValueError(
            "Age status must be approximate or unknown "
            "when birth year is not provided."
        )

    if age_group is not None:
        age_group = age_group.strip()

    with Session(engine) as session:
        try:
            patient = Patient(
                # Temporary unique placeholder replaced before commit.
                patient_code="TEMP",
                patient_name=patient_name,
                birth_year=birth_year,
                age_group=age_group,
                age_status=age_status,
                gender=gender.strip() if gender else None,
                phone=phone.strip() if phone else None,
            )

            session.add(patient)
            session.flush()

            patient.patient_code = f"PAT-{patient.patient_id:04d}"

            session.commit()
            session.refresh(patient)

            return {
                "patient_id": patient.patient_id,
                "patient_code": patient.patient_code,
                "patient_name": patient.patient_name,
                "birth_year": patient.birth_year,
                "age_status": patient.age_status,
            }

        except Exception:
            session.rollback()
            raise


def get_all_patients():
    """Retrieve all registered patients."""

    with Session(engine) as session:
        patients = session.execute(
            select(Patient).order_by(Patient.patient_id.desc())
        ).scalars().all()

        return [
            {
                "Patient ID": patient.patient_id,
                "Patient Code": patient.patient_code,
                "Patient Name": patient.patient_name,
                "Birth Year": patient.birth_year,
                "Age Group": patient.age_group,
                "Age Status": patient.age_status,
                "Gender": patient.gender,
                "Phone": patient.phone,
                "Created At": patient.created_at,
            }
            for patient in patients
        ]


def get_patient_by_id(patient_id):
    """Retrieve one patient using their internal database ID."""

    with Session(engine) as session:
        patient = session.get(Patient, patient_id)

        if patient is None:
            return None

        return {
            "patient_id": patient.patient_id,
            "patient_code": patient.patient_code,
            "patient_name": patient.patient_name,
            "birth_year": patient.birth_year,
            "age_group": patient.age_group,
            "age_status": patient.age_status,
            "gender": patient.gender,
            "phone": patient.phone,
        }
