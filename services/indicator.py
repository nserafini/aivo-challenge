from models.indicator import IndicatorORM

class IndicatorService:

    @classmethod
    def get_by_name(cls, name):
        indicator = IndicatorORM.query.filter_by(name=name).first()
        return indicator