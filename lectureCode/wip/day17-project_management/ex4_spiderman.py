import requests
import json

#Web power!

r = requests.get('https://api.github.com/repos/twitter/bootstrap/forks')
# r = requests.get('https://api.github.com/repos/HampshireCS112/cs112-Spring2012/forks')

#loads = load from string not file object
data = json.loads(r.content)
for i in data:
    print i['owner']['login']