from server import loadClubs


def test_purchase_places(client, test_clubs, test_competitions, setup_mocks):
    places_to_purchase = 8

    response = client.post('/purchasePlaces', data={
        'club': test_clubs[0]['name'],
        'competition': test_competitions[0]['name'],
        'places': places_to_purchase
    })

    assert response.status_code == 200
    assert b'Great-booking complete!' in response.data


def test_max_purchase_places(client, test_clubs, test_competitions, setup_mocks):
    places_to_purchase = 28

    response = client.post('/purchasePlaces', data={
        'club': test_clubs[0]['name'],
        'competition': test_competitions[0]['name'],
        'places': places_to_purchase
    })

    assert response.status_code == 200
    assert b'Max purchase 12.' in response.data


def test_has_sufficient_points(client, test_clubs, test_competitions, setup_mocks):
    places_to_purchase = 9

    response = client.post('/purchasePlaces', data={
        'club': test_clubs[1]['name'],
        'competition': test_competitions[0]['name'],
        'places': places_to_purchase
    })

    assert response.status_code == 200
    assert b'Insufficiant points.' in response.data


def test_update_points_after_purchase(client, test_clubs, test_competitions, setup_mocks):
    places_to_purchase = 9

    response = client.post('/purchasePlaces', data={
        'club': test_clubs[0]['name'],
        'competition': test_competitions[0]['name'],
        'places': str(places_to_purchase)
    })

    assert int(test_clubs[0]['points']) == 4
    assert b'Great-booking complete!' in response.data


def test_login(client):

    response = client.post('/showSummary', data={
        'email': 'john@simplylift.co'
    })
    assert response.status_code == 200


def test_wrong_login(client):

    response = client.post('/showSummary', data={
        'email': 'wrong-email@test.com'
    })
    assert response.status_code == 200
    assert b'Wrong email-please try again' in response.data


def test_display_book_available(client):

    test_club = loadClubs()[0]

    response = client.post('/showSummary', data={'email': test_club['email']})

    assert response.status_code == 200
    assert b'Number of Places: 25' in response.data


def test_display_book_non_available(client, test_competition_full):

    test_club = loadClubs()[0]

    response = client.post('/showSummary', data={'email': test_club['email']})

    assert response.status_code == 200
    assert b'- Competition complete' in response.data


def test_display_points_table(client):

    response = client.get('/clubs-points')
    assert response.status_code == 200
