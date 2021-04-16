from sqlalchemy import Column
from sqlalchemy import String

from models.base import BaseORM


class InequalityORM(BaseORM):

    __tablename__ = "inequalities"

    code = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False, unique=True)