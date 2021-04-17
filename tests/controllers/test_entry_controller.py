from unittest.mock import patch
from app import create_app

app = create_app()
client = app.test_client()

@patch("controllers.entry.EntryService")
def test_entries_controller_get_ok(mock_entry_service):
    mocked_response = ([{"country": "Argentina", "value": 5}], 200)
    mock_entry_service.get_entry.return_value = mocked_response

    indicator = "Labour market insecurity"
    value = 4

    response = client.get(f'/entries/?indicator_name={indicator}&value={value}')
    
    assert response.json == mocked_response[0]
    assert response.status_code == mocked_response[1]

@patch("controllers.entry.EntryService")
def test_entries_controller_get_error_indicator_not_found(mock_entry_service):
    mocked_response = ("Indicator not found", 404)
    mock_entry_service.get_entry.return_value = mocked_response

    indicator = "foo"
    value = 4
    
    response = client.get(f'/entries/?indicator_name={indicator}&value={value}')

    assert response.json == mocked_response[0]
    assert response.status_code == mocked_response[1]

def test_entries_controller_get_error_missing_indicator():
    value = 4
    response = client.get(f'/entries/?value={value}')
    assert response.json['errors'] == {
        'indicator_name': 'Missing required parameter in the JSON body or the post body or the query string'
    }
    assert response.status_code == 400