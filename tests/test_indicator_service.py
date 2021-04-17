from unittest.mock import patch
from unittest.mock import Mock
from services.indicator import IndicatorService
from models import IndicatorORM

@patch("services.indicator.IndicatorORM")
def test_indicator_get_by_name_ok(mock_model):
    mocked_indicator = Mock(id="1", code="JE_LMIS", name="Labour market insecurity")
    mock_model.query.filter_by().first.return_value = mocked_indicator

    indicator_name = 'Labour market insecurity'
    indicator = IndicatorService.get_by_name(indicator_name)
    assert indicator.name == mocked_indicator.name
    assert indicator.code == mocked_indicator.code

@patch("services.indicator.IndicatorORM")
def test_indicator_get_by_name_not_found(mock_model):
    mock_model.query.filter_by().first.return_value = None

    indicator_name = 'foo'
    indicator = IndicatorService.get_by_name(indicator_name)
    assert indicator == None