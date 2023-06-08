from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.account import database
from app.account.repository import accounts
from app.account.models import User

router = APIRouter(
    prefix="/account",
    tags=['Account']
)

get_db = database.get_db

@router.get('/', response_model=None)
def get_users(db: Session = Depends(get_db)):
    return accounts.get_all(db)