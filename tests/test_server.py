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
