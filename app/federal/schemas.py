from typing import Optional

from pydantic import BaseModel

class CountryCreate(BaseModel):
    title: Optional[str]
    title_ne: Optional[str] = None
    code: Optional[str] = None
    order: Optional[int] = 0

class ShowCountry(BaseModel):
    title: Optional[str]
    title_ne: Optional[str]
    code: Optional[str]
    order: Optional[int]

    class Config():
        orm_mode = True

class UpdateCountry(BaseModel):
    title: Optional[str]
    title_ne: Optional[str]
    code: Optional[str]
    order: Optional[int]

class ProvinceCreate(BaseModel):
    title: Optional[str]
    title_ne: Optional[str]
    code: Optional[str] = None
    order: Optional[int] = 0
    country: int

class ShowProvince(BaseModel):
    title: Optional[str]
    title_ne: Optional[str]
    code: Optional[str]
    order: Optional[int]
    country: Optional[int]

    class Config():
        orm_mode = True

class UpdateProvince(BaseModel):
    title: Optional[str]
    title_ne: Optional[str]
    code: Optional[str]
    order: Optional[int]
    country: Optional[int]