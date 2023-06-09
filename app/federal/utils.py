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
    return db

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