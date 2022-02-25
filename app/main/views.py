from flask import render_template
from . import mainBlueprint
from ..models import News_source
from ..models import Article


#Views
@mainBlueprint.route('/')
def index():
    """
    view root page function that returns the index page and its data
    """
    return render_template('index.html')


@mainBlueprint.route('/v2/everything')
def everything(everything):
    
    pass

@mainBlueprint.route('/v2/top-headlines')
def headlines(everything):
    pass

@mainBlueprint.route('/v2/top-headlines/sources')
def source(everything):
    pass
    