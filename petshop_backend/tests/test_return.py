from test_products import get_user_token, get_admin_token
from models.product_m import Product
import uuid

def test_return_requires_token(client):
    response=client.post("/return/FAKE-INVOICE")
    assert response.status_code==401

def test_invalid_invoice(client):
    token=get_user_token(client)
    response=client.post("/return/FUNNY-RETURN", headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code==404

def test_successful_return(client):
    product_name=f"return{uuid.uuid4().hex[:8]}"
    admin_token=get_admin_token(client)
    client.post("/products/", json={
        "name": product_name,
        "description": f"desc{uuid.uuid4().hex[:8]}",
        "price": 25.0,
        "price": 25.0,
        "stock": 100.0 
    },headers={
        "Authorization": f"Bearer {admin_token}"
    })
    product=Product.query.filter_by(name=product_name).first()
    assert product is not None
    product_id=product.id
    initial_stock=product.stock
    user_token=get_user_token(client)
    response=client.post("/cart/add", json={
        "product_id": product_id,
        "quantity": 5
    },headers={
        "Authorization": f"Bearer {user_token}"
    })
    assert response.status_code==201
    checkout_response=client.post("/purchases/checkout", json={
        "billing_address": 1,
        "payment_method": "paypal"
    },headers={
        "Authorization": f"Bearer {user_token}"
    })
    assert checkout_response.status_code==201
    invoice_data=checkout_response.get_json()
    invoice_number=invoice_data["invoice_number"]
    return_response=client.post(f"/return/{invoice_number}",headers={
        "Authorization": f"Bearer {user_token}"
    })
    assert return_response.status_code==200
    data=return_response.get_json()
    assert data["message"]=="Purchase returned successfully."
    product=Product.query.get(product_id)
    assert product.stock==initial_stock

def test_duplicate_return(client):
    product_name=f"duplex_{uuid.uuid4().hex[:8]}"
    admin_token=get_admin_token(client)
    client.post("/products/", json={
        "name": product_name,
        "description":f"desc_{uuid.uuid4().hex[:8]}",
        "price": 25.0,
        "stock": 100
    }, headers={
        "Authorization": f"Bearer {admin_token}"
    })
    product=Product.query.filter_by(name=product_name).first()
    user_token=get_user_token(client)
    client.post("/cart/add", json={
        "product_id": product.id,
        "quantity": 2
    },headers={
        "Authorization": f"Bearer {user_token}"
    })
    checkout_response=client.post("/purchases/checkout", json={
        "billing_address": 1,
        "payment_method": "paypal"
    },headers={
        "Authorization": f"Bearer {user_token}"
    })
    invoice_number=checkout_response.get_json()["invoice_number"]
    client.post(f"/return/{invoice_number}", headers={
        "Authorization": f"Bearer {user_token}"
    })
    response=client.post(f"/return/{invoice_number}", headers={
        "Authorization": f"Bearer {user_token}"
    })
    assert response.status_code==400