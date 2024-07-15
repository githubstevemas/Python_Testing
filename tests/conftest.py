import copy
import pytest
import json

from server import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def test_clubs():
    with open('clubs.json') as c:
        return json.load(c)['clubs']


@pytest.fixture
def test_competitions():
    with open('competitions.json') as comps:
        return json.load(comps)['competitions']
