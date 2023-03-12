def test_get_games_all(client):
    """Get games endpoint returns a list of games. Game objects have required attributes."""
    expected_attributes = {"id", "title", "year", "url", "description"}

    response = client.get("/games")
    payload = response.json()

    assert response.status_code == 200
    assert isinstance(payload, list)
    assert set(payload[0].keys()) == expected_attributes


def test_get_game_found(client):
    """Get game endpoint returns game object with required attributes. Game object retrieved by id is the same as
    one in games all endpoint."""
    expected_attributes = {"id", "title", "year", "url", "description"}
    response_all = client.get("/games")
    game_from_list = response_all.json()[0]

    response = client.get(f"/games/{game_from_list['id']}")
    payload = response.json()

    assert response.status_code == 200
    assert set(payload.keys()) == expected_attributes
    assert payload == game_from_list


def test_get_game_not_found(client):
    """Get game endpoint returns not found response when invalid game id is provided."""
    response_all = client.get("/games")
    id_invalid = max(game["id"] for game in response_all.json()) + 1

    response = client.get(f"/games/{id_invalid}")

    assert response.status_code == 404
    assert "not found" in response.json().get("detail", "").lower()
