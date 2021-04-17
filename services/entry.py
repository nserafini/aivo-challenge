from db import db
from models.country import CountryORM
from models.entry import EntryORM
from services.indicator import IndicatorService
from services.inequality import InequalityService

class EntryService:

    @classmethod
    def get_entry(cls, filters):

        indicator = IndicatorService.get_by_name(filters.get("indicator_name"))
        if not indicator:
            return "Indicator not found", 404

        inequality = InequalityService.get_by_name("Total")
        if not inequality:
            return "Inequality not found", 404

        entries = db.session.query(EntryORM, CountryORM).join(
            CountryORM, EntryORM.country_id == CountryORM.id
        ).filter(
            EntryORM.indicator_id == indicator.id, 
            EntryORM.inequality_id == inequality.id, 
            EntryORM.value > filters.get("value")
        ).all()
        
        if not entries:
            return "Entry not found", 404
            
        entries = [{
            'country': u[1].to_dict()['name'], 
            'value':u[0].to_dict()['value']
        } for u in entries]

        
        return entries, 200