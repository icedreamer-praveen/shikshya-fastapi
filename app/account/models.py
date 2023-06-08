from enum import Enum

from sqlalchemy import Boolean, Column, Date, DateTime
from sqlalchemy import Enum as SQLAlchemyEnum
from sqlalchemy import ForeignKey, Integer, String

from .database import Base


class RoleEnum(str, Enum):
    Tutor = 'Tutor'
    Student = 'Student'

class GenderEnum(str, Enum):
    Male = 'Male'
    Female = 'Female'
    NonBinary = 'None-Binary'
    Prefer_Not_To_Sepcify = 'Prefer Not To Specify'
    Others = 'Others'


class User(Base):
    __tablename__='users'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(64))
    middle_name = Column(String(64), nullable=True)
    last_name = Column(String(64))
    dob = Column(Date)
    email = Column(String, unique=True, index=True)
    position = Column(String(255), nullable=True)
    role = Column(String(15), SQLAlchemyEnum(RoleEnum))
    gender = Column(String(25), SQLAlchemyEnum(GenderEnum))
    contact = Column(String(17))
    city = Column(String(100), nullable=True)
    city_ne = Column(String(125), nullable=True)
    # country = Column(Integer, ForeignKey('country.id', ondelete='CASCADE'), back_populates='country')
    # province = Column(Integer, ForeignKey('province.id', ondelete='SET NULL'), back_populates='province', default=None, nullable=True)
    # district = Column(Integer, ForeignKey('district.id', ondelete='SET NULL'), back_populates='district', default=None, nullable=True)
    # municipality = Column(Integer, ForeignKey('municipality.id', ondelete='SET NULL'), back_populates='municipality', default=None, nullable=True)
    verfication_link_expiration = Column(DateTime, nullable=True)
    is_verified = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
