def test_index(client):
    response = client.get("")

    assert b"Welcome to Holiday Homes" in response.content
    assert b"Lettings" in response.content
    assert b"Profiles" in response.content
