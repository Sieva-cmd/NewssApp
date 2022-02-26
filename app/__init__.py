from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from newsapi import NewsApiClient


bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    
    #creating application configuration
    app.config.from_object(config_options[config_name])
    
    #initializing flask extensions
    bootstrap.init_app(app)
    
    #Registering the blueprint
    from .main import mainBlueprint as main_blueprint
    app.register_blueprint(main_blueprint)
    
    #setting config
    from .requests import configure_request
    configure_request(app)
    
    
    #will add the views and forms
    
    return app