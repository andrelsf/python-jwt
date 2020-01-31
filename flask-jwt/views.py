from run import app
from flask import jsonify

@app.route('/ping')
def pong():
    return jsonify({
        'message': 'Pong'
    })