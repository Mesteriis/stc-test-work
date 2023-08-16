from datetime import datetime

from pydantic import BaseModel

from models.task import StatusEnum
from .employeer import EmployeesStruct

class TaskStruct(BaseModel):
    id: int
    name: str
    description: str
    status: StatusEnum
    employee_id: int
    parent_id: int
    deadline: datetime

class TaskCreateStruct(BaseModel):
    name: str
    description: str
    status: StatusEnum
    employee_id: int
    parent_id: int
    deadline: datetime


class TaskImportantStruct(BaseModel):
    task: TaskStruct
    deadline: datetime
    employees: list[EmployeesStruct]
