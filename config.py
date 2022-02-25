import os

from flask import Config
class Convig:
    NEWS_BASE_API_URL ='https://newsapi.org/v2/everything?q=Apple&from=2022-02-25&sortBy={}&apiKey={}'
    NEWS_API_KEY =os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    
    
config_options ={
    'development':DevConfig,
    'production':ProdConfig
}        
    
    
