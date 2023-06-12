from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.federal import models, schemas


def create(request: schemas.CountryCreate, db: Session):
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

def get_all(db: Session):
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
            detail=f"Country with the id {id} is not found."
        )
    db.delete(country)
    db.commit()
    return {
        "message": "Country deleted successfully"
    }