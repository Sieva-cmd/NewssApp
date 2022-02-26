from flask import render_template
from . import mainBlueprint
from requests import get_news



#Views
@mainBlueprint.route('/')
def index():
    """
    view root page function that returns the index page and its data
    """
    title ="World news"
    news =get_news()
    return render_template('index.html', title =title, articles =news)


@mainBlueprint.route('/v2/everything')
def everything():
    
    pass

@mainBlueprint.route('/v2/top-headlines')
def top_headlines():
    pass

@mainBlueprint.route('/v2/top-headlines/sources')
def source():
    pass

@mainBlueprint.route('/everything')
def search():
    pass
    
    