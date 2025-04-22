from sqlalchemy.orm import Session
from app import models, schemas

# Create a new task
def create_task(db: Session, title: str, description: str):
    db_task = models.Task(title=title, description=description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# Get all tasks
def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Task).offset(skip).limit(limit).all()
