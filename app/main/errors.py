from flask import render_template
from . import mainBlueprint
@mainBlueprint.app_errorhandler(404)
def foour_ow_four(error):
    """
    function to return the 404 error page
    """
    return render_template('fourOwFour.html'),404