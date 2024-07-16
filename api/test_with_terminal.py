import pytest
import requests


@pytest.fixture
def url_status(request) -> tuple:
    url = request.config.getoption("--url")
    status = request.config.getoption("--status_code")
    return url, status


def test_response(url_status):
    url, status = url_status
    response = requests.post(url)
    assert response.status_code == int(status)