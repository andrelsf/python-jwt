from run import app
from flask import jsonify

@app.route('/')
def index():
    return pong()

@app.route('/ping')
def pong():
    return jsonify({
        'message': 'Pong'
    })