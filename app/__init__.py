from ensurepip import bootstrap
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options,DevConfig


bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)
    
    #initialized app configuration
    app.config.from_object(config_name)
    
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    
    return app