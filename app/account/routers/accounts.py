from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.account import database, schemas
from app.account.models import User
from app.account.repository import accounts

router = APIRouter(
    prefix="/account",
    tags=['Account']
)

get_db = database.get_db

@router.get('/', response_model=None)
def get_users(db: Session = Depends(get_db)):
    """
    This function retrieves all users from the database.
    
    :param db: The parameter `db` is of type `Session` and is a dependency that is obtained using the
    `get_db` function. It is used to access the database and perform CRUD (Create, Read, Update, Delete)
    operations on the `accounts` table. The `get_all` function is
    :type db: Session
    :return: The function `get_users` is returning the result of calling the `get_all` function from the
    `accounts` module, passing in the `db` parameter. The specific data being returned depends on the
    implementation of the `get_all` function, but it is likely a list of user objects or a database
    query result containing user data.
    """
    return accounts.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    This function creates a new user in the database using the provided user creation request and
    database session.
    
    :param request: The request parameter is an instance of the UserCreate schema, which is used to
    validate and deserialize the incoming request data. It contains the data required to create a new
    user account, such as the user's email, password, and full name
    :type request: schemas.UserCreate
    :param db: The parameter `db` is a database session object that is obtained using the `get_db`
    dependency. It is used to interact with the database and perform CRUD (Create, Read, Update, Delete)
    operations on the user data. The `db` parameter is passed as an argument to the `
    :type db: Session
    :return: The `create` function is returning the result of calling the `create` function from the
    `accounts` module, passing in the `request` and `db` arguments. The specific return value will
    depend on the implementation of the `create` function in the `accounts` module.
    """
    return accounts.create(request, db)