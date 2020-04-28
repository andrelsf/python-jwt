from run import app
from flask import json
from werkzeug.exceptions import HTTPException

"""
    Handler Errors 400 e 404
"""
@app.errorhandler(HTTPException)
def handleException(error):
    """
        Return JSON instead of HTML for HTTP errors.
    """
    response = error.get_response()
    response.data = json.dumps({
        "code": error.code,
        "name": error.name,
        "description": error.description
    })
    response.content_type = "application/json"
    return response