import pytest
import json

import server
from server import app, competitions


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def test_clubs():
    with open('tests/test_clubs.json') as c:
        return json.load(c)['clubs']


@pytest.fixture
def test_competitions():
    with open('tests/test_competitions.json') as comps:
        return json.load(comps)['competitions']


@pytest.fixture
def test_competition_full():
    competitions[:] = [
        {'name': 'Test Comptetition #3',
         'date': '2020-03-27 10:00:00',
         'numberOfPlaces': '0'}
    ]


@pytest.fixture
def setup_mocks(mocker, test_clubs, test_competitions):
    mocker.patch.object(server, 'clubs', test_clubs)
    mocker.patch.object(server, 'competitions', test_competitions)
    mocker.patch('server.saveClub')
