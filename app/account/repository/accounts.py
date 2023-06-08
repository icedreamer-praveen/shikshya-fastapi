from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.account import models, schemas

def get_all(db: Session):
    users = db.query(models.User).all()
    return users