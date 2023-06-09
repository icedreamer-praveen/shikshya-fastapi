from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.account import models, schemas


def create(reqquest: schemas.UserCreate, db: Session):
    """
    The function creates a new user in the database using the provided user information.
    
    :param reqquest: The parameter `reqquest` is of type `schemas.UserCreate`, which is a Pydantic model
    representing the data required to create a new user
    :type reqquest: schemas.UserCreate
    :param db: The "db" parameter is an instance of the SQLAlchemy Session class, which is used to
    interact with the database. It allows the function to perform database operations such as adding a
    new user, committing changes, and refreshing the user object with the latest data from the database
    :type db: Session
    :return: the newly created user object.
    """
    new_user = models.User(
        first_name=reqquest.first_name,
        middle_name=reqquest.middle_name,
        last_name=reqquest.last_name,
        dob=reqquest.dob,
        email=reqquest.email,
        position=reqquest.position,
        role=reqquest.role,
        gender=reqquest.gender,
        contact=reqquest.contact,
        city=reqquest.city,
        city_ne=reqquest.city_ne,
        country_id=reqquest.country_id,
        province_id=reqquest.province_id,
        district_id=reqquest.district_id,
        municipality_id=reqquest.municipality_id,
        is_verified=reqquest.is_verified,
        is_active=reqquest.is_active
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all(db: Session):
    """
    The function retrieves all users from a database using SQLAlchemy.
    
    :param db: Session
    :type db: Session
    :return: The function `get_all` returns a list of all the users in the database.
    """
    users = db.query(models.User).all()
    return users

def get_user(id: int, db: Session):
    """
    This function retrieves a user from a database by their ID and raises an exception if the user is
    not found.
    
    :param id: The id parameter is an integer that represents the unique identifier of a user in the
    database
    :type id: int
    :param db: The "db" parameter is a SQLAlchemy session object that is used to interact with the
    database. It allows the function to query the database and retrieve the user with the specified ID
    :type db: Session
    :return: a user object from the database with the specified id. If the user is not found, it raises
    an HTTPException with a 400 status code and a message indicating that the user with the specified id
    is not found.
    """
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"user with the id {id} is not found."
        )
    return user