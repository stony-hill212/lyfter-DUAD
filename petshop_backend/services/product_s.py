from models.product_m import Product
from extensions import db, cache
from schemas.product_schema import products_schema, product_schema
from repositories.product_repo import ProductRepo
from exceptions.api_exceptions import NotFoundError, BadRequestError

def create_product(data):
    existing_product=Product.query.filter(
        (
            Product.name==data["name"]
        ) |
        (
            Product.description==data["description"]
        )
    ).first()
    if existing_product:
        raise BadRequestError(
            "Product already exists."
        )
    new_product=Product(
        name=data["name"],
        description=data.get("description"),
        price=data["price"],
        stock=data["stock"]
    )
    ProductRepo.add(new_product)
    cache.clear()
    return{
        "message": "Product created successfully.",
        "product_id": new_product.id
    }

def get_all_products():
    products=ProductRepo.get_all()
    print("Fetching products.")
    return products_schema.dump(products)

def get_product(product_id):
    product=ProductRepo.get_by_id(product_id)
    if not product:
        raise NotFoundError("Product not found.")
    return product_schema.dump(product)

def update_products(product_id, data):
    product=ProductRepo.get_by_id(product_id)
    if not product:
        raise NotFoundError("Product not found.")
    product.name=data.get("name", product.name)
    product.description=data.get("description", product.description)
    product.price=data.get("price", product.price)
    product.stock=data.get("stock", product.stock)
    ProductRepo.commit()
    cache.delete("view//products/")
    cache.delete_memoized(get_product)
    return{"message": "Product update successfully."}

def delete_product(product_id):
    product=ProductRepo.get_by_id(product_id)
    if not product:
        raise NotFoundError("Product not found.")
    ProductRepo.delete(product)
    cache.delete("view//products/")
    cache.delete_memoized(get_product)
    return{"message": "Product deleted successfully"}