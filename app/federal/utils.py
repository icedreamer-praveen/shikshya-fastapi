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

def delete_province(id: int, db: Session):
    """
    This function deletes a province from the database based on its ID.
    
    :param id: The id parameter is an integer that represents the unique identifier of the province that
    needs to be deleted from the database
    :type id: int
    :param db: The "db" parameter is an instance of the SQLAlchemy Session class, which is used to
    interact with the database. It allows the code to perform database operations such as querying,
    inserting, updating, and deleting data. The Session class provides a transactional scope for all the
    operations performed within it, which
    :type db: Session
    :return: a dictionary with a message indicating that the province was deleted successfully.
    """
    province = db.query(models.Province).filter(models.Province.id == id).first()
    if province is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Province with the id {id} is not found"
        )
    db.delete(province)
    db.commit()
    return {
        "message": "Province deleted successfully"
    }

def update_province(id: int, request: schemas.UpdateProvince, db: Session):
    """
    This function updates a province in the database based on the provided ID and request data.
    
    :param id: The id parameter is an integer that represents the unique identifier of the province that
    needs to be updated
    :type id: int
    :param request: The `request` parameter is of type `schemas.UpdateProvince`, which is a Pydantic
    model representing the fields that can be updated for a `Province` object. The
    `dict(exclude_unset=True)` method call on `request` returns a dictionary of the fields and their
    values that have been
    :type request: schemas.UpdateProvince
    :param db: The "db" parameter is a database session object that is used to interact with the
    database. It is passed as an argument to the function and is used to query and update the database.
    The session object is typically created using a database engine and a connection pool, and it
    provides a transactional scope
    :type db: Session
    :return: an instance of the updated province model.
    """
    province = db.query(models.Province).filter(models.Province.id == id).first()
    if province is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Province with the id {id} is not found"
        )
    for field, value in request.dict(exclude_unset=True).items():
        setattr(province, field, value)

    db.commit()
    db.refresh(province)
    return province

def patch_province(id: int, request: schemas.UpdateProvince, db: Session):
    """
    This function updates a province in the database based on the provided ID and request data.
    
    :param id: The ID of the province that needs to be updated
    :type id: int
    :param request: The request parameter is of type schemas.UpdateProvince, which is a Pydantic model
    that defines the fields that can be updated for a Province object. It contains the following fields:
    :type request: schemas.UpdateProvince
    :param db: The `db` parameter is an instance of a database session, which is used to interact with
    the database and perform CRUD (Create, Read, Update, Delete) operations on the `Province` model. It
    is passed as an argument to the function so that the function can access the database and make
    :type db: Session
    :return: an instance of the updated province model.
    """
    province = db.query(models.Province).filter(models.Province.id == id).first()
    if province is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Province with the id {id} is not found"
        )
    if request.title:
        province.title = request.title
    if request.title_ne:
        province.title_ne = request.title_ne
    if request.code:
        province.code = request.code
    if request.order:
        province.order = request.order
    if request.country:
        province.country = request.country

    db.commit()
    db.refresh(province)
    return province


def create_district(request: schemas.DistrictCreate, db: Session):
    """
    This function creates a new district object in the database based on the provided request data.
    
    :param request: The request parameter is an instance of the DistrictCreate class defined in the
    schemas module. It contains the data required to create a new district in the database, including
    the district's title, title in Nepali language, code, order, and the province it belongs to
    :type request: schemas.DistrictCreate
    :param db: The "db" parameter is a database session object that is used to interact with the
    database. It is passed as an argument to the function and is used to add the newly created district
    object to the database, commit the changes, and refresh the object to ensure that it reflects any
    changes made during the
    :type db: Session
    :return: The function `create_district` returns an instance of the `District` model that has been
    created and added to the database.
    """
    district = models.District(
        title = request.title,
        title_ne = request.title_ne,
        code = request.code,
        order = request.order,
        province = request.province
    )
    db.add(district)
    db.commit()
    db.refresh(district)
    return district


def get_all_district(db: Session):
    """
    This function retrieves all districts from a database using SQLAlchemy.
    
    :param db: Session object from SQLAlchemy. It is used to interact with the database and perform CRUD
    operations
    :type db: Session
    :return: The function `get_all_district` returns a list of all the districts in the database.
    """
    district = db.query(models.District).all()
    return district

def get_district(id: int, db: Session):
    """
    The function retrieves a district from a database based on its ID and raises an exception if it is
    not found.
    
    :param id: The id parameter is an integer representing the unique identifier of a district
    :type id: int
    :param db: The "db" parameter is a SQLAlchemy Session object, which is used to interact with the
    database. It allows us to execute queries and perform CRUD (Create, Read, Update, Delete) operations
    on the database
    :type db: Session
    :return: a district object from the database that matches the given id. If no district is found, it
    raises an HTTPException with a 404 status code and a message indicating that the district with the
    given id is not found.
    """
    district = db.query(models.District).filter(models.District.id == id).first()
    if district is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"District with the id {id} is not found"
        )
    return district

def delete_district(id: int, db: Session):
    """
    This function deletes a district from the database based on its ID.
    
    :param id: The id parameter is an integer that represents the unique identifier of the district that
    needs to be deleted from the database
    :type id: int
    :param db: The "db" parameter is an instance of the SQLAlchemy Session class, which is used to
    interact with the database. It allows the code to perform database operations such as querying,
    inserting, updating, and deleting data. The Session class provides a transactional scope for all the
    operations performed within it, which
    :type db: Session
    :return: a dictionary with a message indicating that the district was deleted successfully.
    """
    district = db.query(models.District).filter(models.District.id == id).first()
    if district is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"District with the id {id} is not found"
        )
    db.delete(district)
    db.commit()
    return {
        "message": "District deleted successfully"
    }

def update_district(id: int, request: schemas.UpdateDistrict, db: Session):
    """
    This function updates a district in the database based on the provided ID and request data.
    
    :param id: The id parameter is an integer that represents the unique identifier of the district that
    needs to be updated
    :type id: int
    :param request: The request parameter is of type schemas.UpdateDistrict, which is a Pydantic model
    representing the data to be updated for a district. It contains the fields and their updated values
    for the district. The exclude_unset=True argument in the request.dict() method ensures that only the
    fields that have been updated are
    :type request: schemas.UpdateDistrict
    :param db: The "db" parameter is a database session object that is used to interact with the
    database. It is an instance of the SQLAlchemy Session class, which provides a high-level interface
    for managing database transactions. The session object is used to query the database, make changes
    to the data, and commit those changes
    :type db: Session
    :return: an instance of the updated district model.
    """
    district = db.query(models.District).filter(models.District.id == id).first()
    if district is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"District with the id {id} is not found"
        )
    for field, value in request.dict(exclude_unset=True).items():
        setattr(district, field, value)

    db.commit()
    db.refresh(district)
    return district

def patch_district(id: int, request: schemas.UpdateDistrict, db: Session):
    """
    This function updates a district in the database based on the provided request data.
    
    :param id: The id parameter is an integer that represents the unique identifier of the district that
    needs to be updated
    :type id: int
    :param request: The request parameter is of type schemas.UpdateDistrict, which is a Pydantic model
    that defines the fields that can be updated for a district. It contains the following fields:
    :type request: schemas.UpdateDistrict
    :param db: The `db` parameter is a database session object that allows the function to interact with
    the database. It is used to query and update the database. The `Session` type indicates that this is
    a SQLAlchemy session object
    :type db: Session
    :return: an instance of the updated district model.
    """
    district = db.query(models.District).filter(models.District.id == id).first()
    if district is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"District with the id {id} is not found"
        )
    if request.title:
        district.title = request.title
    if request.title_ne:
        district.title_ne = request.title_ne
    if request.code:
        district.code = request.code
    if request.order:
        district.order = request.order
    if request.province:
        district.province = request.province

    db.commit()
    db.refresh(district)
    return district