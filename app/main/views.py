from unicodedata import category
from urllib import request
from flask import render_template,redirect,request
from . import mainBlueprint
from ..requests import get_news,get_sources





#Views
@mainBlueprint.route('/')
def index():
    """
    view root page function that returns the index page and its data
    """
    title ="World news"
    news =get_news()
    return render_template('index.html', title =title, articles =news)


@mainBlueprint.route('/sources')
def sources():
    news =get_sources()
    
    return render_template('news.html',sources=news)
    

    
    