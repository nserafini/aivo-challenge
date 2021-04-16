from sqlalchemy import Column
from sqlalchemy import String

from models.base import BaseORM


class CountryORM(BaseORM):

    __tablename__ = "countries"

    code = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False, unique=True)