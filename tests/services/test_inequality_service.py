from unittest.mock import patch
from unittest.mock import Mock
from services.inequality import InequalityService
from models import InequalityORM

@patch("services.inequality.InequalityORM")
def test_inequality_get_by_name_ok(mock_model):
    mocked_inequality = Mock(id="1", code="TOT", name="Total")
    mock_model.query.filter_by().first.return_value = mocked_inequality

    inequality_name = 'Total'
    inequality = InequalityService.get_by_name(inequality_name)
    assert inequality.name == mocked_inequality.name
    assert inequality.code == mocked_inequality.code

@patch("services.inequality.InequalityORM")
def test_inequality_get_by_name_not_found(mock_model):
    mock_model.query.filter_by().first.return_value = None

    inequality_name = 'foo'
    inequality = InequalityService.get_by_name(inequality_name)
    assert inequality == None