from fixture.application import Application
import pytest

@pytest.fixture
def app():
    fixture = Application(host='https://api.apteka.tech')
    return fixture

