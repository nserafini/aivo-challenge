from sqlalchemy import Column
from sqlalchemy import String

from models.base import BaseORM


class IndicatorORM(BaseORM):

    __tablename__ = "indicators"

    code = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False, unique=True)