def test_smoke_root_response(client):
    """Root endpoint returns OK response with simple JSON."""
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"status": "OK"}
