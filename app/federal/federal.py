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

@router.get('/{id}/', status_code=status.HTTP_200_OK, response_model=schemas.ShowCountry)
def get_country(id: int, db: Session = Depends(get_db)):
    """
    This function retrieves a country from a database based on its ID.
    
    :param id: The id parameter is an integer that represents the unique identifier of a country in a
    database
    :type id: int
    :param db: db is a parameter of type Session that is used to access the database. It is obtained
    using the get_db function which returns a new session for each request. The session is used to query
    the database and perform CRUD operations. The Session object is provided by the SQLAlchemy ORM
    (Object-Relational Mapping
    :type db: Session
    :return: The function `get_country()` is returning the result of calling the `utils.get_country()`
    function with the `id` parameter and the `db` parameter obtained from the `get_db()` function. The
    specific return value depends on the implementation of the `utils.get_country()` function.
    """
    return utils.get_country(id, db)

@router.delete('/{id}/', status_code=status.HTTP_202_ACCEPTED, response_model=None)
def delete_country(id: int, db: Session = Depends(get_db)):
    """
    This function deletes a country from the database based on its ID.
    
    :param id: The id parameter is an integer that represents the unique identifier of a country in the
    database. It is used to identify the country that needs to be deleted
    :type id: int
    :param db: The parameter `db` is of type `Session` and is a dependency that is obtained using the
    `get_db` function. It is used to access the database and perform CRUD (Create, Read, Update, Delete)
    operations on the `Country` table. The `Session` object represents a
    :type db: Session
    :return: The function `delete_country()` is being returned, which takes two arguments: `id` of type
    `int` and `db` of type `Session`. The function is defined in a separate module called `utils` and is
    responsible for deleting a country from the database based on the given `id`. The `db` argument is a
    dependency that is obtained using the `get_db()` function.
    """
    return utils.delete_country(id, db)