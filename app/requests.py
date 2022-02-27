
import urllib.request,json
from .models import Articles,News_source
# from newsapi import NewsApiClient

#getting api_key
api_key =None
#Getting base_url
base_url =None
base_source_url =None

def configure_request(app):
    global api_key,base_url,base_source_url
    
    api_key =app.config['NEWS_API_KEY']
    base_url =app.config['NEWS_API_BASE_URL']
    base_source_url =app.config['NEWS_SOURCE_BASE_URL']
    
    
    # api_key =NewsApiClient(api_key='NEWS_API_KEY')

    # base_url =NewsApiClient(api_key='NEWS_API_BASE_URL')
    
    # top_headlines = newsapi.get_top_headlines(language='en',page='20',sources='bbc-news')
    # all_articles = top_headlines('articles')
    # sources = newsapi.get_sources()
    
def get_news():
    get_news_url =  base_url.format(api_key)
    
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data =url.read()
        get_news_response =json.loads(get_news_data)
        
        news_results =None
        
        if get_news_response['articles']:
            news_results_list =get_news_response['articles']
            news_results =process_results(news_results_list)
            
    return news_results


def process_results(news_list):
    news_result =[]
    for news_item in news_list:
        title =news_item.get('title')
        description =news_item.get('description')
        urlToImage =news_item.get('urlToImage')
        content =news_item.get('content')
        publishedAt =news_item.get('publishedAt')
        url =news_item.get('url')
        
        news_object =Articles(title,description,urlToImage,content,publishedAt,url)
        news_result.append(news_object)
        
    return news_result   
         
def get_sources():
    
    get_sources_url =base_source_url.format(api_key)
    
    
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_source_response =json.loads(get_sources_data)
        source_results =None
        if get_source_response['sources']:
            source_results_list =get_source_response['sources']
            source_results=process_source_results(source_results_list)
    return source_results


def process_source_results(source_list):
    source_result =[]
    
    for source_item in source_list:
        name =source_item.get('name')
        description =source_item.get('description')
        url =source_item.get('url')
        
        source_object =News_source(name,description,url)
        source_result.append(source_object)
        
        
    return source_result    
                
        
               
    
    

