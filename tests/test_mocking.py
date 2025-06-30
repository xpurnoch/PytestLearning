import pytest
import requests
import source.database_to_mock as lm
import unittest.mock as mock

@mock.patch('source.database_to_mock.get_user')
def test_get_user(mock_get_user):
    mock_get_user.return_value = "Mocked Alice"
    user = lm.get_user(1)
    assert user == "Mocked Alice"

@mock.patch('requests.get')
def test_fetch_users(mock_requests_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"id": 1, "name": "John Doe"}]
    mock_requests_get.return_value = mock_response
    data = lm.fetch_users()
    assert data == [{"id": 1, "name": "John Doe"}]

@mock.patch('requests.get')
def test_fetch_users_failure(mock_requests_get):
    mock_response = mock.Mock()
    mock_response.status_code = 404
    mock_requests_get.return_value = mock_response
    with pytest.raises(requests.HTTPError):
        lm.fetch_users()
