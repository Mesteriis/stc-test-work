from src.core.db import Base
from sqlalchemy import Column, Integer, String


class EmployeesModel(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    job = Column(String(255), nullable=False)

