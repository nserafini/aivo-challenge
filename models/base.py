from uuid import uuid4

from sqlalchemy import Column
from sqlalchemy import String

from db import db

def get_uuid():
    return str(uuid4())

class BaseORM(db.Model):

    __abstract__ = True

    id = Column(String, primary_key=True, default=get_uuid, unique=True)

    def to_dict(self):
        model_dict = dict(self.__dict__)
        model_dict.pop('_sa_instance_state')
        return model_dict