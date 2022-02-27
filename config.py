import os

# from flask import Config
class Config:
    NEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines?country=us&apiKey=88678b63f3da49bc968e8956f7a783bd'
    NEWS_API_KEY =os.environ.get('88678b63f3da49bc968e8956f7a783bd')
    # SECRET_KEY = os.environ.get('SECRET_KEY')
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    
    
config_options ={
    'development':DevConfig,
    'production':ProdConfig
}        
    
    
