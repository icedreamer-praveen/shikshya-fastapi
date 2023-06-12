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

class UpdateProvince(BaseModel):
    title: Optional[str]
    title_ne: Optional[str]
    code: Optional[str]
    order: Optional[int]
    country: Optional[int]

class ShowProvince(BaseModel):
    title: Optional[str]
    title_ne: Optional[str]
    code: Optional[str]
    order: Optional[int]
    country: Optional[int]

    class Config():
        orm_mode = True


class DistrictCreate(BaseModel):
    title: Optional[str]
    title_ne: Optional[str]
    code: Optional[str] = None
    order: Optional[int] = 0
    province: int

class UpdateDistrict(BaseModel):
    title: Optional[str]
    title_ne: Optional[str]
    code: Optional[str]
    order: Optional[int]
    province: Optional[int]

class ShowDistrict(BaseModel):
    title: Optional[str]
    title_ne: Optional[str]
    code: Optional[str]
    order: Optional[int]
    province: Optional[int]

    class Config():
        orm_mode = True


class MunicipalityCreate(BaseModel):
    title: Optional[str]
    title_ne: Optional[str]
    code: Optional[str] = None
    order: Optional[int] = 0
    district: int

class UpdateMunicipality(BaseModel):
    title: Optional[str]
    title_ne: Optional[str]
    code: Optional[str]
    order: Optional[int]
    district: Optional[int]

class ShowMunicipality(BaseModel):
    title: Optional[str]
    title_ne: Optional[str]
    code: Optional[str]
    order: Optional[int]
    district: Optional[int]

    class Config():
        orm_mode = True