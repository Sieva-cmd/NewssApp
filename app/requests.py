from turtle import title
import urllib.request,json
from .models import Articles
from .models import News_source
from newsapi import NewsApiClient

#getting api_key
api_key =None
#Getting base_url
base_url =None

def configure_request(app):
    global api_key,base_url
    
    api_key =app.config['NEWS_API_KEY']
    base_url =app.config['NEWS_API_BASE_URL']
    
    
    # api_key =NewsApiClient(api_key='NEWS_API_KEY')

    # base_url =NewsApiClient(api_key='NEWS_API_BASE_URL')
    
    # top_headlines = newsapi.get_top_headlines(language='en',page='20',sources='bbc-news')
    # all_articles = top_headlines('articles')
    # sources = newsapi.get_sources()
    
def get_news():
    get_news_url =base_url.format(api_key)
    
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data =url.read()
        get_news_response =json.loads(get_news_data)
        
        news_results =None
        
        if get_news_response['articles']:
            news_results_list =get_news_response['articles']
            news_results =process_results(news_results_list)
            
    return news_results


def process_results(news_list):
    news_results =[]
    for news_item in news_list:
        title =news_item.get('title')
        description =news_item.get('description')
        urlToImage =news_item.get('urlToImage')
        content =news_item.get('content')
        publishedAt =news_item('publishedAt')
        
        news_object =Articles(title,description,urlToImage,content,publishedAt)
        news_results.append(news_object)
        
    return news_results    
        
         
    
    

