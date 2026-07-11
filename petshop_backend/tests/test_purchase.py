import sys, uuid
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from test_products import get_user_token, get_admin_token
from models.product_m import Product

def test_checkout_empty_cart(client):
    token=get_user_token(client)
    response=client.post("/purchases/checkout", json={
        "billing_address": 1,
        "payment_method": "cash"
    },headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code in [400, 404, 500]

def test_successful_checkout(client):
    product_name=f"testing{uuid.uuid4().hex[:8]}"
    description=f"testing{uuid.uuid4().hex[:8]}"
    admin_token=get_admin_token(client)
    create_response=client.post("/products/", json={
        "name": product_name,
        "description": description,
        "price": 30.0,
        "stock": 70
    },headers={
        "Authorization": f"Bearer {admin_token}"
    })
    print(create_response.status_code)
    print(create_response.get_json())
    assert create_response.status_code==201
    product=Product.query.filter_by(name=product_name).first()
    assert product is not None
    product_id=product.id
    token=get_user_token(client)
    cart_response=client.post("/cart/add", json={
        "product_id": product_id,
        "quantity": 2
    },headers={
        "Authorization": f"Bearer {token}"
    })
    assert cart_response.status_code==201
    
    checkout_response=client.post(
        "/purchases/checkout", json={
            "billing_address": 1,
            "payment_method": "cash"
        },headers={
            "Authorization": f"Bearer {token}"
        }
    )
    assert checkout_response.status_code==201
    data=checkout_response.get_json()
    assert data["purchase_id"]>0
    assert data["invoice_number"].startswith("INV-")
