from typing import Optional

from pydantic import BaseModel

class CountryCreate(BaseModel):
    title: str
    title_ne: Optional[str] = None
    code: Optional[str] = None
    order: Optional[int] = 0

class ShowCountry(BaseModel):
    title: str
    title_ne: Optional[str]
    code: Optional[str]
    order: Optional[str]

    class Config():
        orm_mode = True
