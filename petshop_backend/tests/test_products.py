import sys, uuid
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from werkzeug.security import generate_password_hash
from models.user_m import User
from extensions import db

def test_get_products_requires_token(client):
    response=client.get("/products/")
    assert response.status_code==401

def get_admin_token(client):
    email=f"conventional_{uuid.uuid4().hex[:8]}@fight.com"
    admin=User(
        username=f"orthodox_{uuid.uuid4().hex[:8]}",
        email=email,
        password=generate_password_hash("1234567"),
        role="admin"
    )
    db.session.add(admin)
    db.session.commit()
    response=client.post("/auth/login",json={
        "email": email,
        "password": "1234567"
    })
    return response.get_json()["access_token"]

def test_create_product(client):
    name=f"testing{uuid.uuid4().hex[:8]}"
    description=f"testing{uuid.uuid4().hex[:8]}"
    token=get_admin_token(client)
    response=client.post(
        "/products/",
        json={
            "name": name,
            "description": description,
            "price": 2.98,
            "stock": 2000
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )
    assert response.status_code==201

def test_get_products(client, app):
    token=get_admin_token(client)
    response=client.get("/products/", headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code==200

def get_user_token(client):
    email=f"lefty_{uuid.uuid4().hex[:8]}@fight.com"
    user=User(
        username=f"southpaw_{uuid.uuid4().hex[:8]}",
        email=email,
        password=generate_password_hash("1234567"),
        role="user",
    )
    db.session.add(user)
    db.session.commit()
    response=client.post("/auth/login", json={
        "email": email,
        "password": "1234567"
    })
    return response.get_json()["access_token"]

def test_user_cannot_create(client):
    token=get_user_token(client)
    response=client.post("/products/",json={
        "name": "Funny product",
        "description": "test",
        "price": 10,
        "stock": 10
    },headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code==403

def test_product_not_found(client):
    token=get_admin_token(client)
    response=client.get("/products/99999", headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code==404