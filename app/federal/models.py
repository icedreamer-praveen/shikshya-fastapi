from sqlalchemy import ForeignKey, Column, Integer, String

from app.account.database import Base


class Country(Base):
    __tablename__='country'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    title_ne = Column(String(255), nullable=True)
    code = Column(String(25), nullable=True)
    order = Column(Integer, default=0, nullable=True)

class Province(Base):
    __tablename__='province'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    title_ne = Column(String(255), nullable=True)
    code = Column(String(25), default=None, nullable=True)
    order = Column(Integer, default=0, nullable=True)
    country = Column(Integer, ForeignKey('country.id', ondelete='RESTRICT'), back_populates='country_province')

class District(Base):
    __tablename__='district'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    title_ne = Column(String(255), nullable=True)
    code = Column(String(25), default=None, nullable=True)
    order = Column(Integer, default=0, nullable=True)
    province = Column(Integer, ForeignKey('province.id', ondelete='RESTRICT'), back_populates='province_district')

class Municipality(Base):
    __tablename__='municipality'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    title_ne = Column(String(255), nullable=True)
    code = Column(String(25), nullable=True, default=None)
    order = Column(Integer, default=0, nullable=True)
    district = Column(Integer, ForeignKey('district.id', ondelete='RESTRICT', back_populates='district_municipality'))


