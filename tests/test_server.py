import server
from server import loadCompetitions, loadClubs


def test_purchase_places(client):
    test_club = loadClubs()[0]
    test_competition = loadCompetitions()[0]
    places_to_purchase = 8

    response = client.post('/purchasePlaces', data={
        'club': test_club['name'],
        'competition': test_competition['name'],
        'places': places_to_purchase
    })

    assert response.status_code == 200
    assert b'Great-booking complete!' in response.data


def test_max_purchase_places(client):
    test_club = loadClubs()[0]
    test_competition = loadCompetitions()[0]
    places_to_purchase = 28

    response = client.post('/purchasePlaces', data={
        'club': test_club['name'],
        'competition': test_competition['name'],
        'places': places_to_purchase
    })

    assert response.status_code == 200
    assert b'Max purchase 12.' in response.data


def test_has_sufficient_points(client):
    test_club = loadClubs()[1]
    test_competition = loadCompetitions()[0]
    places_to_purchase = 9

    response = client.post('/purchasePlaces', data={
        'club': test_club['name'],
        'competition': test_competition['name'],
        'places': places_to_purchase
    })

    assert response.status_code == 200
    assert b'Insufficiant points.' in response.data


def test_purchase_places(client, test_clubs, test_competitions, mocker):

    mocker.patch('server.loadClubs', return_value=test_clubs)
    mocker.patch('server.loadCompetitions', return_value=test_competitions)
    mock_save_club = mocker.patch('server.saveClub')

    mocker.patch.object(server, 'clubs', test_clubs)
    mocker.patch.object(server, 'competitions', test_competitions)

    places_to_purchase = 9

    response = client.post('/purchasePlaces', data={
        'club': test_clubs[0]['name'],
        'competition': test_competitions[0]['name'],
        'places': str(places_to_purchase)
    })

    assert int(test_clubs[0]['points']) == 4
    assert b'Great-booking complete!' in response.data
