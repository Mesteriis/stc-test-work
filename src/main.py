from fastapi import FastAPI
from config import settings
from fastapi import APIRouter
from fastapi_crudrouter import SQLAlchemyCRUDRouter

from core.db import get_session, Base
from models import TasksModel
from structures import TaskStruct, TaskCreateStruct

app = FastAPI(
    title=settings.title,
    description=settings.project_description,
    version=settings.project_version,
)

tasks_router = APIRouter(prefix="/tasks", tags=['tasks'])


@tasks_router.get("", response_model=list[TaskStruct])
def get_tasks():
    return get_session().query(TasksModel).all()


@tasks_router.post("", response_model=TaskStruct)
def create_task(task: TaskCreateStruct):
    task = TasksModel(**task.model_dump())
    session = get_session()
    session.add(task)
    session.commit()
    return task


@tasks_router.delete("/{task_id}")
def delete_task(task_id: int):
    session = get_session()
    session.query(TasksModel).filter(TasksModel.id == task_id).delete()
    session.commit()
    return {"message": "Task deleted successfully"}


@tasks_router.put("/{task_id}")
def update_task(task_id: int, task: TaskCreateStruct):
    session = get_session()
    session.query(TasksModel).filter(TasksModel.id == task_id).update(task.model_dump())
    session.commit()
    return {"message": "Task updated successfully"}


app.include_router(tasks_router)
