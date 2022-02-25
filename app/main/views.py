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