from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr, constr

from app.account.models import GenderEnum, RoleEnum


class UserBase(BaseModel):
    class Config:
        use_enum_values = True

class UserCreate(UserBase):
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    dob: date
    email: EmailStr
    position: Optional[str] = None
    role: RoleEnum
    gender: GenderEnum
    contact: constr(regex=r'^\+?[1-9][0-9]{7,14}$')
    city: Optional[str] = None
    city_ne: Optional[str] = None
    country: int
    province: Optional[int] = None
    district: Optional[int] = None
    municipality: Optional[int] = None
    is_verified: bool = False
    is_active: bool = False


class ShowUser(BaseModel):
    id: int
    first_name: str
    middle_name: Optional[str]
    last_name: str
    email: str
    gender: str
    role: str
    dob: date
    contact: str
    city: str
    city_ne: Optional[str]
    position: str
    is_active: bool
    is_verified: bool

    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

