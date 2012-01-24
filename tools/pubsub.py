import requests
from bottle import app, run, post, route, request

@post('/recv')
def recieve_json():
    print request.files