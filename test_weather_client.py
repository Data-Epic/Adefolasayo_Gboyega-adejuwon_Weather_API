import pytest
from weather_client import get_weather_data, get_future_weather_data
import requests
import json


def test_city_input_correct(monkeypatch):
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: 'Lagos')
        city_name = input("Enter the city name:")
        assert city_name == 'Lagos'
        
def test_city_input_incorrect(monkeypatch):
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: '123')
        city_name = input("Enter the city name:")
        assert isinstance(city_name, str)
        assert city_name == '123'
        

def test_get_weather_data_proper_api_connection_success(monkeypatch):
    """Test for a proper connection to the API (successful response)."""
    # Mock a successful API response (status code 200) with necessary keys
    mock_weather_data = {
        'name': 'Lekki',
        'main': {'temp': 302.15, 'humidity': 75, 'pressure': 1011},
        'weather': [{'description': 'scattered clouds'}]
    }
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = json.dumps(mock_weather_data).encode('utf-8') # Realistic mock data

    def mock_get(*args, **kwargs):
        return mock_response

    monkeypatch.setattr(requests, 'get', mock_get)

    result = get_weather_data('Lekki', should_print=False)
    assert result is not None, "Should return data (even if mocked) for a successful connection"



def test_get_weather_data_proper_api_connection_failure(monkeypatch):
    """Test for a proper connection to the API (failed response)."""
    # Mock a failed API response (status code other than 200)
    mock_response = requests.Response()
    mock_response.status_code = 404

    def mock_get(*args, **kwargs):
        return mock_response

    monkeypatch.setattr(requests, 'get', mock_get)

    result = get_weather_data('InvalidCity', should_print=False)
    assert result is None, "Should return None for a failed API connection"