from flask import Flask
from .extensions import db, jwt, swagger
from .routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")
    
    jwt.init_app(app)
    swagger.init_app(app)
    db.init_app(app)
        
    register_routes(app)
    
    return app