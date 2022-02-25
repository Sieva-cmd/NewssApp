import urllib.request,json
from .models import News_source
from .models import Article

#getting api_key
api_key =None
#Getting base_url
base_url =None

def configure_request(app):
    global api_key,base_url
    api_key =app.config['NEWS_API_KEY']
    base_url=app.config['NEWS_API_BASE_URL']
    
