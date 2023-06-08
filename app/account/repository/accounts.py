from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.account import models, schemas


def get_all(db: Session):
    users = db.query(models.User).all()
    return users

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
        # country_id=reqquest.country_id,
        # province_id=reqquest.province_id,
        # district_id=reqquest.district_id,
        # municipality_id=reqquest.municipality_id,
        # verification_link_expiration=reqquest.verification_link_expiration,
        is_verified=reqquest.is_verified,
        is_active=reqquest.is_active
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user