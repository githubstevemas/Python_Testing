import pytest
import json

from server import app, competitions


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


@pytest.fixture
def test_competition_full():
    competitions[:] = [
        {'name': 'Spring Festival',
         'date': '2020-03-27 10:00:00',
         'numberOfPlaces': '0'}
    ]
