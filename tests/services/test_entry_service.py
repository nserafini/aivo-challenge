from unittest.mock import patch
from services.entry import EntryService
from models import EntryORM
from models import CountryORM

@patch("services.entry.InequalityService")
@patch("services.entry.IndicatorService")
@patch("services.entry.db")
def test_get_entry_ok(mock_db, mock_indicator, mock_inequality):

    mock_db.session.query().join().filter().all.return_value = [(
        EntryORM(country_id="1", indicator_id="1", inequality_id="1", value=6),
        CountryORM(code="ARG", name="Argentina")
    )]

    filters = {
        'indicator_name': 'Labour market insecurity', 
        'value': 5
    }
    response, status = EntryService.get_entry(filters)
    assert status == 200
    assert response[0]["country"] == "Argentina"
    assert response[0]["value"] == 6

@patch("services.entry.IndicatorService")
def test_get_entry_indicator_not_found(mock_indicator):

    mock_indicator.get_by_name.return_value = None

    filters = {
        'indicator_name': 'Labour market insecurity', 
        'value': 5
    }
    response, status = EntryService.get_entry(filters)
    assert status == 404
    assert response == "Indicator not found"

@patch("services.entry.InequalityService")
@patch("services.entry.IndicatorService")
def test_get_entry_inequality_not_found(mock_indicator, mock_inequality):

    mock_inequality.get_by_name.return_value = None

    filters = {
        'indicator_name': 'Labour market insecurity', 
        'value': 5
    }
    response, status = EntryService.get_entry(filters)

    assert status == 404
    assert response == "Inequality not found"