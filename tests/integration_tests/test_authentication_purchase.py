

def test_complete_purchase(client, test_clubs, test_competitions, setup_mocks):

    # testing index display
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome' in response.data

    # testing points table display
    response = client.get('/clubs-points')
    assert response.status_code == 200
    assert b'Clubs points' in response.data

    # testing user connexion
    response = client.post('/showSummary', data={
        'email': 'john@test.com'
    })
    assert response.status_code == 200
    assert b'Welcome' in response.data

    # testing purchase display
    places_to_purchase = 8
    response = client.post('/purchasePlaces', data={
        'club': test_clubs[0]['name'],
        'competition': test_competitions[0]['name'],
        'places': places_to_purchase
    })
    assert response.status_code == 200
    assert b'Great-booking complete!' in response.data
    assert int(test_clubs[0]['points']) == 5

    # testing user logout
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'Please enter your secretary email' in response.data
