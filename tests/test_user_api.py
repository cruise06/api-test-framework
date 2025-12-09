def test_get_user(user_service):
    resp = user_service.get_user(1)
    assert resp.status_code == 200
    data = resp.json()
    assert data["id"] == 1
