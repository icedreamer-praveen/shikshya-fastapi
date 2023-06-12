from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.federal import schemas, utils
from app.account import database

get_db = database.get_db

router = APIRouter(
    prefix="/federal",
    tags=['Federal']
)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.CountryCreate, db: Session = Depends(get_db)):
    """
    This function creates a new country record in the database using the provided request data.
    
    :param request: The request parameter is an instance of the CountryCreate schema, which is used to
    validate and deserialize the incoming request data. It contains the data needed to create a new
    country in the database
    :type request: schemas.CountryCreate
    :param db: The "db" parameter is a database session object that is created using the "get_db"
    function. It is used to interact with the database and perform CRUD (Create, Read, Update, Delete)
    operations. The session object is passed as a dependency to the function using the "Depends"
    :type db: Session
    :return: The `create` function is returning the result of calling the `utils.create` function with
    the `request` and `db` arguments. The specific return value depends on the implementation of the
    `utils.create` function.
    """
    return utils.create(request, db)

@router.get('/', status_code=status.HTTP_200_OK, response_model=None)
def get_all(db: Session = Depends(get_db)):
    """
    This function retrieves all data from a database using a helper function.
    
    :param db: The parameter `db` is a dependency injection that is used to get a database session
    object. It is of type `Session` which is a class from the SQLAlchemy library that represents a
    connection to a database. The `Depends` function is used to declare a dependency on the `get_db`
    :type db: Session
    :return: The function `get_all` is returning the result of calling the `get_all` function from the
    `utils` module, passing in the `db` parameter. The specific return value depends on the
    implementation of the `get_all` function in the `utils` module.
    """
    return utils.get_all(db)