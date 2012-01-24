import sys
import getpass
import json

import requests
from bottle import app, run, post, route, request

def subscribe():
    r = requests.post("https://api.github.com/hub", data={"hub.mode": "subscribe", "hub.topic": "https://github.com/HampshireCS/cs143-Spring2012/events/push", "hub.callback": "http://icepick.stdnt.hampshire.edu/githacks/"}, auth=("jrabbit", getpass.getpass()))
    print r.content

@post('/')
def recieve_json():
    x = json.loads(request.forms.payload)
    print x
@route('/')
def index():
    print "Nothing here for you to see."
if __name__ == '__main__':
    if '-setup' in sys.argv:
        subscribe()
    run(host='localhost', port=9999)