from models.inequality import InequalityORM

class InequalityService:

    @classmethod
    def get_by_name(cls, name):
        inequality = InequalityORM.query.filter_by(name=name).first()
        return inequality