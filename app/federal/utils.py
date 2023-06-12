from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.federal import models, schemas


def create_country(request: schemas.CountryCreate, db: Session):
    """
    The function creates a new country object in the database based on the input data.
    
    :param request: The request parameter is of type schemas.CountryCreate, which is a Pydantic model
    representing the data required to create a new country. It contains the following fields:
    :type request: schemas.CountryCreate
    :param db: The "db" parameter is an instance of the SQLAlchemy Session class, which is used to
    interact with the database. It is passed to the function as an argument so that the function can
    perform database operations such as adding a new country to the database
    :type db: Session
    :return: the database session object (`db`) after adding and committing a new `Country` object to
    the database.
    """
    country = models.Country(
        title = request.title,
        title_ne = request.title_ne,
        code = request.code,
        order = request.order
    )
    db.add(country)
    db.commit()
    db.refresh(country)
    return country

def get_all_country(db: Session):
    """
    This function retrieves all the country records from the database using SQLAlchemy's query method.
    
    :param db: Session
    :type db: Session
    :return: The function `get_all` returns a list of all the `Country` objects in the database accessed
    through the provided `Session` object.
    """
    country = db.query(models.Country).all()
    return country

def get_country(id: int, db: Session):
    """
    This function retrieves a country from a database based on its ID and raises an exception if the
    country is not found.
    
    :param id: The id parameter is an integer that represents the unique identifier of a country in the
    database
    :type id: int
    :param db: The "db" parameter is a database session object that is used to query the database and
    retrieve data. It is likely an instance of a database session class provided by an ORM
    (Object-Relational Mapping) library such as SQLAlchemy. The session object is used to execute
    queries and commit changes to the
    :type db: Session
    :return: a country object from the database with the specified id. If the country is not found, it
    raises an HTTPException with a 400 status code and a message indicating that the country with the
    specified id is not found.
    """
    country = db.query(models.Country).filter(models.Country.id == id).first()
    if not country:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"country with the id {id} is not found."
        )
    return country

def delete_country(id: int, db: Session):
    """
    This function deletes a country from the database based on its ID.
    
    :param id: The id parameter is an integer that represents the unique identifier of the country that
    needs to be deleted from the database
    :type id: int
    :param db: The "db" parameter is an instance of the SQLAlchemy Session class, which is used to
    interact with the database. It allows the function to query, add, update, and delete records from
    the database. The Session class manages the transactional state of the database, ensuring that
    changes are committed or rolled
    :type db: Session
    :return: a dictionary with a message indicating that the country was deleted successfully.
    """
    country = db.query(models.Country).filter(models.Country.id == id).first()
    if country is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Country with the id {id} is not found"
        )
    db.delete(country)
    db.commit()
    return {
        "message": "Country deleted successfully"
    }

def update_country(id: int, request: schemas.UpdateCountry, db: Session):
    """
    This function updates a country in the database based on the provided ID and request data.
    
    :param id: The id parameter is an integer that represents the unique identifier of the country that
    needs to be updated
    :type id: int
    :param request: schemas.UpdateCountry is a Pydantic model that defines the fields that can be
    updated for a country. It is used to validate the request body sent by the client
    :type request: schemas.UpdateCountry
    :param db: The parameter `db` is a database session object. It is used to interact with the database
    and perform CRUD (Create, Read, Update, Delete) operations on the data. The session object is
    created using a database engine and represents a transactional scope, which means that all changes
    made to the
    :type db: Session
    :return: an instance of the updated country model.
    """
    country = db.query(models.Country).filter(models.Country.id == id).first()
    if country is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"country with the id {id} is not found"
        )
    for field, value in request.dict(exclude_unset=True).items():
        setattr(country, field, value)

    db.commit()
    db.refresh(country)
    return country

def patch_country(id: int, request: schemas.UpdateCountry, db: Session):
    """
    This function updates a country in the database based on the provided ID and request data.
    
    :param id: The ID of the country that needs to be updated
    :type id: int
    :param request: The request parameter is of type schemas.UpdateCountry, which is a Pydantic model
    representing the data to be updated for a country. It contains four optional fields: title,
    title_ne, code, and order
    :type request: schemas.UpdateCountry
    :param db: The `db` parameter is a database session object, which is used to interact with the
    database and perform CRUD (Create, Read, Update, Delete) operations on the data. It is passed as an
    argument to the function so that the function can access the database and make changes to it. The
    :type db: Session
    :return: an instance of the updated country model.
    """
    country = db.query(models.Country).filter(models.Country.id == id).first()
    if country is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Country with the id {id} is not found"
        )
    if request.title:
        country.title = request.title
    if request.title_ne:
        country.title_ne = request.title_ne
    if request.code:
        country.code = request.code
    if request.order:
        country.order = request.order

    db.commit()
    db.refresh(country)
    return country


def create_province(request: schemas.ProvinceCreate, db: Session):
    """
    This function creates a new province in the database based on the provided request data.
    
    :param request: schemas.ProvinceCreate - This is a Pydantic model that defines the structure of the
    request body for creating a new province. It contains the following fields: title (str), title_ne
    (str), code (str), order (int), and country (str)
    :type request: schemas.ProvinceCreate
    :param db: The "db" parameter is a database session object that is used to interact with the
    database. It is passed as an argument to the function and is used to add the newly created province
    object to the database, commit the changes, and refresh the object to ensure that it reflects any
    changes made during the
    :type db: Session
    :return: The function `create_province` returns an instance of the `Province` model that has been
    created and added to the database.
    """
    province = models.Province(
        title = request.title,
        title_ne = request.title_ne,
        code = request.code,
        order = request.order,
        country = request.country
    )
    db.add(province)
    db.commit()
    db.refresh(province)
    return province


def get_all_province(db: Session):
    """
    This function retrieves all provinces from a database using SQLAlchemy.
    
    :param db: The parameter `db` is of type `Session`. It is likely that this function is part of a
    larger application that uses an Object Relational Mapper (ORM) such as SQLAlchemy to interact with a
    database. The `Session` object represents a transactional scope for interacting with the database.
    It provides
    :type db: Session
    :return: The function `get_all_province` returns a list of all the provinces in the database.
    """
    province = db.query(models.Province).all()
    return province

def get_province(id: int, db: Session):
    """
    The function retrieves a province from a database based on its ID and raises an exception if it is
    not found.
    
    :param id: The id parameter is an integer that represents the unique identifier of a province
    :type id: int
    :param db: The "db" parameter is a SQLAlchemy Session object, which is used to interact with the
    database. It allows the function to execute queries and perform CRUD (Create, Read, Update, Delete)
    operations on the database
    :type db: Session
    :return: The function `get_province` returns a `Province` object from the database that matches the
    given `id`. If no such object is found, it raises an HTTPException with a 404 status code and a
    message indicating that the province with the given id was not found.
    """
    province = db.query(models.Province).filter(models.Province.id == id).first()
    if province is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Province with the id {id} is not found"
        )
    return province