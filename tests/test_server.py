from server import loadCompetitions, loadClubs


def test_purchase_places(client):

    clubs = loadClubs()
    competitions = loadCompetitions()

    test_club = clubs[0]
    test_competition = competitions[0]
    places_to_purchase = 8

    response = client.post('/purchasePlaces', data={
        'club': test_club['name'],
        'competition': test_competition['name'],
        'places': places_to_purchase
    })

    assert response.status_code == 200
    assert b'Great-booking complete!' in response.data


def test_max_purchase_places(client):

    clubs = loadClubs()
    competitions = loadCompetitions()

    test_club = clubs[0]
    test_competition = competitions[0]
    places_to_purchase = 28

    response = client.post('/purchasePlaces', data={
        'club': test_club['name'],
        'competition': test_competition['name'],
        'places': places_to_purchase
    })

    assert response.status_code == 200
    assert b'Max purchase 12.' in response.data
