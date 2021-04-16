from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import UniqueConstraint
from sqlalchemy import ForeignKey

from models.base import BaseORM


class EntryORM(BaseORM):

    __tablename__ = "entries"

    country_id = Column(ForeignKey("countries.id"), nullable=False)
    indicator_id = Column(ForeignKey("indicators.id"), nullable=False)
    inequality_id = Column(ForeignKey("inequalities.id"), nullable=False)
    value = Column(Float, nullable=False)

    __table_args__ = (
        UniqueConstraint(country_id, indicator_id, inequality_id),
    )