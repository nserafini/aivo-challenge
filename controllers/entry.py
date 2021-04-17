from flask_restplus import Namespace
from flask_restplus import reqparse
from flask_restplus import Resource

from services.entry import EntryService

entries_ns = Namespace('entries')

@entries_ns.route('/')
class EntriesController(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('indicator_name', type=str, required=True)
    parser.add_argument('value', type=float, required=True)

    @entries_ns.expect(parser)
    def get(self):
        filters = self.parser.parse_args()
        return EntryService.get_entry(filters)