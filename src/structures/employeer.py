from core.db import Base
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel, ConfigDict


class EmployeesStruct(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    job: str
