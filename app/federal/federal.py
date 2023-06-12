from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.federal import schemas, utils
from app.account import database

get_db = database.get_db

router = APIRouter(
    prefix="/federal",
    tags=['Federal']
)

@router.post('/country/', status_code=status.HTTP_201_CREATED)
def create_country(request: schemas.CountryCreate, db: Session = Depends(get_db)):
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
    return utils.create_country(request, db)

@router.get('/countries/', status_code=status.HTTP_200_OK, response_model=None)
def get_all_country(db: Session = Depends(get_db)):
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
    return utils.get_all_country(db)

@router.get('/country/{id}/', status_code=status.HTTP_200_OK, response_model=schemas.ShowCountry)
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

@router.delete('/country/{id}/', status_code=status.HTTP_202_ACCEPTED, response_model=None)
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

@router.put('/country/{id}/', status_code=status.HTTP_200_OK, response_model=None)
def update_country(id: int, request: schemas.UpdateCountry, db: Session = Depends(get_db)):
    """
    This function updates a country in the database based on the provided ID and request data.
    
    :param id: The ID of the country that needs to be updated
    :type id: int
    :param request: schemas.UpdateCountry is likely a Pydantic model/schema that defines the structure
    and data types of the request body for updating a country in the API. It could include fields such
    as the country's name, population, capital city, etc
    :type request: schemas.UpdateCountry
    :param db: The "db" parameter is a database session object that is passed to the function using the
    "Depends" function from the FastAPI framework. This session object is used to interact with the
    database and perform CRUD (Create, Read, Update, Delete) operations on the "Country" table. The
    :type db: Session
    :return: The function `update_country` is returning the result of calling the `utils.update_country`
    function with the provided parameters `id`, `request`, and `db`. The specific return value of
    `utils.update_country` will depend on the implementation of that function.
    """
    return utils.update_country(id, request, db)

@router.patch('/country/{id}/', status_code=status.HTTP_200_OK, response_model=None)
def patch_country(id: int, request: schemas.UpdateCountry, db: Session = Depends(get_db)):
    """
    This function patches a country in the database with the provided ID and request data.
    
    :param id: an integer representing the ID of the country to be updated
    :type id: int
    :param request: The `request` parameter is of type `schemas.UpdateCountry`, which is a Pydantic
    model representing the data to be updated for a country in the database. This parameter is used by
    the `utils.patch_country` function to update the country record in the database
    :type request: schemas.UpdateCountry
    :param db: The "db" parameter is a dependency injection that provides a database session to the
    function. It is used to interact with the database and perform CRUD (Create, Read, Update, Delete)
    operations. The "Session" type is likely referring to a SQLAlchemy session object
    :type db: Session
    :return: The function `patch_country` is returning the result of calling the `utils.patch_country`
    function with the provided arguments `id`, `request`, and `db`. The specific return value will
    depend on the implementation of the `utils.patch_country` function.
    """
    return utils.patch_country(id, request, db)


@router.post('/province/', status_code=status.HTTP_201_CREATED)
def create_province(request: schemas.ProvinceCreate, db: Session = Depends(get_db)):
    """
    This function creates a province using the provided request data and database connection.
    
    :param request: The request parameter is an instance of the ProvinceCreate schema, which is used to
    validate and deserialize the incoming request data for creating a new province. It contains the
    necessary fields and their data types for creating a new province, such as the province name,
    country ID, and population
    :type request: schemas.ProvinceCreate
    :param db: db is a parameter that represents the database session. It is of type Session, which is a
    class provided by the SQLAlchemy library. The session is used to interact with the database and
    perform CRUD (Create, Read, Update, Delete) operations on the database tables. The session is
    created and managed by
    :type db: Session
    :return: The function `create_province` is returning the result of calling the
    `utils.create_province` function with the `request` and `db` arguments. The specific return value
    depends on the implementation of the `utils.create_province` function.
    """
    return utils.create_province(request, db)

@router.get('/provinces/', status_code=status.HTTP_200_OK, response_model=None)
def get_all_province(db: Session = Depends(get_db)):
    """
    This function retrieves all provinces from a database using a helper function.
    
    :param db: The parameter `db` is of type `Session` and is used as a dependency for the function
    `get_all_province()`. It is likely that `get_db()` is a function that returns a database session
    object, which is then passed as an argument to `get_all_province()`. The session
    :type db: Session
    :return: The function `get_all_province` is returning the result of calling the `get_all_province`
    function from the `utils` module with the `db` parameter passed as an argument. The specific return
    value depends on the implementation of the `get_all_province` function in the `utils` module.
    """
    return utils.get_all_province(db)


@router.get('/province/{id}/', status_code=status.HTTP_200_OK, response_model=schemas.ShowProvince)
def get_province(id: int, db: Session = Depends(get_db)):
    """
    This function retrieves a province from a database based on its ID.
    
    :param id: The id parameter is an integer that represents the unique identifier of a province. It is
    used to retrieve information about a specific province from the database
    :type id: int
    :param db: The parameter `db` is a dependency injection that is used to get a database session. It
    is of type `Session` which is a class from the SQLAlchemy library that represents a transactional
    database session. The `get_db` function is responsible for creating a new database session for each
    request and closing
    :type db: Session
    :return: The function `get_province` is returning the result of calling the `utils.get_province`
    function with the `id` parameter and the `db` parameter obtained from the `get_db` dependency.
    """
    return utils.get_province(id, db)

@router.delete('/province/{id}/', status_code=status.HTTP_202_ACCEPTED, response_model=None)
def delete_province(id: int, db: Session = Depends(get_db)):
    """
    This function deletes a province from the database based on its ID.
    
    :param id: The id parameter is an integer that represents the unique identifier of a province that
    needs to be deleted from the database
    :type id: int
    :param db: The parameter `db` is of type `Session` and is a dependency that is obtained using the
    `get_db` function. It is used to access the database and perform CRUD (Create, Read, Update, Delete)
    operations on the `Province` table. The `Session` object represents a
    :type db: Session
    :return: The function `delete_province` is being returned, which takes two arguments: `id` of type
    `int` and `db` of type `Session`. The function is defined in a separate module called `utils`. The
    purpose of the function is to delete a province from the database based on the given `id`. The
    function is executed using the `db` session obtained from the `get_db
    """
    return utils.delete_province(id, db)

@router.put('/province/{id}/', status_code=status.HTTP_200_OK, response_model=None)
def update_province(id: int, request: schemas.UpdateProvince, db: Session = Depends(get_db)):
    """
    This function updates a province in the database based on the provided ID and request data.
    
    :param id: The ID of the province that needs to be updated
    :type id: int
    :param request: schemas.UpdateProvince is a Pydantic model that defines the structure of the request
    body for updating a province. It likely contains fields such as the province name, population, and
    other relevant information that can be updated
    :type request: schemas.UpdateProvince
    :param db: The "db" parameter is a database session object that is passed to the function using the
    "Depends" function from the FastAPI framework. This allows the function to access the database and
    perform CRUD (Create, Read, Update, Delete) operations on the "Province" table. The session object
    :type db: Session
    :return: The function `update_province` is returning the result of calling the
    `utils.update_province` function with the provided arguments `id`, `request`, and `db`. The specific
    return value of `utils.update_province` is not specified in this code snippet.
    """
    return utils.update_province(id, request, db)

@router.patch('/province/{id}/', status_code=status.HTTP_200_OK, response_model=None)
def patch_province(id: int, request: schemas.UpdateProvince, db: Session = Depends(get_db)):
    """
    This function patches a province in the database with the provided ID and update request.
    
    :param id: an integer representing the ID of the province to be updated
    :type id: int
    :param request: schemas.UpdateProvince is likely a Pydantic model that defines the structure and
    validation rules for the request body of a PATCH request to update a province in a database. It
    could contain fields such as name, population, area, etc
    :type request: schemas.UpdateProvince
    :param db: The "db" parameter is a dependency injection that provides a database session to the
    function. It is used to interact with the database and perform CRUD (Create, Read, Update, Delete)
    operations. The "Session" type is imported from the SQLAlchemy library and represents a connection
    to the database. The
    :type db: Session
    :return: The function `patch_province` is returning the result of calling the `utils.patch_province`
    function with the provided arguments `id`, `request`, and `db`. The specific return value will
    depend on the implementation of the `utils.patch_province` function.
    """
    return utils.patch_province(id, request, db)



@router.post('/district/', status_code=status.HTTP_201_CREATED)
def create_district(request: schemas.DistrictCreate, db: Session = Depends(get_db)):
    return utils.create_district(request, db)

@router.get('/districts/', status_code=status.HTTP_200_OK, response_model=None)
def get_all_district(db: Session = Depends(get_db)):
    return utils.get_all_district(db)


@router.get('/district/{id}/', status_code=status.HTTP_200_OK, response_model=schemas.ShowDistrict)
def get_district(id: int, db: Session = Depends(get_db)):
    return utils.get_district(id, db)

@router.delete('/district/{id}/', status_code=status.HTTP_202_ACCEPTED, response_model=None)
def delete_district(id: int, db: Session = Depends(get_db)):
    return utils.delete_district(id, db)

@router.put('/district/{id}/', status_code=status.HTTP_200_OK, response_model=None)
def update_district(id: int, request: schemas.UpdateDistrict, db: Session = Depends(get_db)):
    return utils.update_district(id, request, db)

@router.patch('/district/{id}/', status_code=status.HTTP_200_OK, response_model=None)
def patch_district(id: int, request: schemas.UpdateDistrict, db: Session = Depends(get_db)):
    return utils.patch_district(id, request, db)

