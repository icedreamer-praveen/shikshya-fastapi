from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.account import database, models, schemas, token, utils

from .hashing import Hash

router = APIRouter(
    prefix="/account",
    tags=['Account']
)

get_db = database.get_db


@router.post('/login/')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    """
    This function handles user login authentication and returns an access token.
    
    :param request: The `request` parameter is of type `OAuth2PasswordRequestForm` and is used to
    retrieve the user's email and password from the request body. It is a dependency injected by
    FastAPI's `Depends()` function and is used to validate the user's credentials during the login
    process
    :type request: OAuth2PasswordRequestForm
    :param db: The "db" parameter is a dependency injection that provides a database session to the
    function. It is used to query the database for the user's email and password
    :type db: Session
    :return: a dictionary with two keys: "access_token" and "token_type". The value of "access_token" is
    a JWT access token generated using the user's email as the subject, and the value of "token_type" is
    "bearer".
    """
    user = db.query(models.User).filter(
        models.User.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Invalid Credentials"
        )
    if not Hash.verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Incorrect password"
        )
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

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
    `utils` module, passing in the `request` and `db` arguments. The specific return value will
    depend on the implementation of the `create` function in the `utils` module.
    """
    return utils.create(request, db)

@router.get('/', response_model=None)
def get_users(db: Session = Depends(get_db)):
    """
    This function retrieves all users from the database.
    
    :param db: The parameter `db` is of type `Session` and is a dependency that is obtained using the
    `get_db` function. It is used to access the database and perform CRUD (Create, Read, Update, Delete)
    operations on the `utils` table. The `get_all` function is
    :type db: Session
    :return: The function `get_users` is returning the result of calling the `get_all` function from the
    `utils` module, passing in the `db` parameter. The specific data being returned depends on the
    implementation of the `get_all` function, but it is likely a list of user objects or a database
    query result containing user data.
    """
    return utils.get_all(db)

@router.get('/{id}/', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    """
    This function retrieves a user from a database by their ID.
    
    :param id: The id parameter is an integer that represents the unique identifier of a user. It is
    used to retrieve information about a specific user from the database
    :type id: int
    :param db: The parameter `db` is a dependency injection that is used to get a database session. It
    is of type `Session` which is a SQLAlchemy session object. The `Depends` function is used to declare
    the dependency on the `get_db` function which returns a database session. This allows the
    :type db: Session
    :return: The function `get_user` is returning the result of calling the `utils.get_user` function
    with the `id` and `db` arguments. The specific return value depends on the implementation of the
    `utils.get_user` function.
    """
    return utils.get_user(id, db)