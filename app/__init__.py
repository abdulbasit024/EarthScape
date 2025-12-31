from flask import Flask
from config import Config
from .extensions import db, login_manager

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    
    # Import models to ensure they are registered with SQLAlchemy
    from app import models

    # Register blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    # Create database tables automatically in development mode
    if app.debug:
        with app.app_context():
            db.create_all()

    return app
