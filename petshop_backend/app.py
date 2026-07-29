from flask import Flask
from config import Config
from extensions import db, jwt, migrate, cache, ma
from models import address_m, cart_item_m, cart_m, invoice_m, product_m, purchase_m, user_m, purchase_item_m
from routes.auth_r import auth_bp
from routes.product_r import product_bp
from utils.error_handlers import register_error_handlers
from routes.cart_r import cart_bp
from routes.purchase_r import purchase_bp
from routes.address_r import address_bp
from routes.invoice_r import invoice_bp
from routes.return_r import return_bp
from routes.user_r import user_bp
from routes.purchase_query_r import purchase_query_bp

def create_app():
    app=Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)

    app.register_blueprint(auth_bp,url_prefix="/auth")
    app.register_blueprint(product_bp,url_prefix="/products")
    app.register_blueprint(cart_bp,url_prefix="/cart")
    app.register_blueprint(purchase_bp,url_prefix="/purchases")
    app.register_blueprint(address_bp,url_prefix="/addresses")
    app.register_blueprint(invoice_bp,url_prefix="/invoice")
    app.register_blueprint(return_bp,url_prefix="/return")
    app.register_blueprint(user_bp,url_prefix="/users")
    app.register_blueprint(purchase_query_bp)

    register_error_handlers(app)
    
    return app

app=create_app()

if __name__=="__main__":
    app.run(debug=True)