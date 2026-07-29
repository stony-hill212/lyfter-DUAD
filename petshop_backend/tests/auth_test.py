import uuid

def test_profile_requires_token(client):
    response=client.get("/auth/profile")
    assert response.status_code==401

def test_register_user(client):
    response=client.post("/auth/register",json={
        "username":f"poopies_{uuid.uuid4().hex[:8]}j",
        "email":f"poopies_{uuid.uuid4().hex[:8]}@jackass.com",
        "password": "1234567",
    })
    assert response.status_code==201

def test_login_user(client):
    response=client.post("/auth/login",json={
        "email": "pytest@test.com",
        "password": "1234567"
    })
    print(response.status_code)
    print(response.get_json())
    assert response.status_code==200