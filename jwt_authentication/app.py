from flask import Flask
from config import Config
from extensions import db, jwt, migrate
from models.user import User
from routes.auth import auth_bp
from routes.me import me_bp
from routes.fruits_r import fruit_bp
from routes.purchase import purchase_bp
from routes.invoice_r import invoice_bp

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    app.register_blueprint(auth_bp)
    app.register_blueprint(me_bp)
    app.register_blueprint(fruit_bp)
    app.register_blueprint(purchase_bp)
    app.register_blueprint(invoice_bp)
    return app

app=create_app()

with app.app_context():
    db.create_all()
    print("Tables created!")

if __name__=="__main__":
    app.run(debug=True)