
from datetime import datetime

from sqlalchemy import (
    Column,
    Date,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class MedicalRecord(Base):
    __tablename__ = "medical_records"

    id = Column(Integer, primary_key=True, autoincrement=True)

    # Link each medical record to a registered patient.
    # NULL is allowed for existing records whose owners are unknown.
    patient_id = Column(
        Integer,
        ForeignKey(
            "patients.patient_id",
            ondelete="RESTRICT",
            onupdate="CASCADE",
        ),
        nullable=True,
    )

    patient = relationship("Patient", back_populates="medical_records")

    test_name = Column(String(100), nullable=False)
    value = Column(Float, nullable=False)
    unit = Column(String(30), nullable=False)

    # Keep existing historical age information.
    patient_age = Column(Integer, nullable=False)
    test_date = Column(Date, nullable=False)

    source = Column(String(50), nullable=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    def __repr__(self):
        return (
            f"MedicalRecord(id={self.id}, "
            f"patient_id={self.patient_id}, "
            f"test_name='{self.test_name}', "
            f"value={self.value}, unit='{self.unit}')"
        )