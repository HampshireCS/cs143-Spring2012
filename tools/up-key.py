import requests
import getpass
import json
import os
import os.path

REPO_NAME = "cs112-Spring2012"
REPO_ORG = "HampshireCS112"

keyfile = os.path.join(os.path.expanduser("~"), ".ssh/id_rsa.pub")
if not os.path.exists(keyfile):
    os.system('ssh-keygen')
key = open(keyfile).readlines()[0].strip()
name = raw_input("Github Username: ")
keyjson = json.dumps({"title": "Auto-added key for %s" % name, "key": key})
auth = (name, getpass.getpass("Github Password:"))

def do_gh(url, method="post", **kw):
    method = getattr(requests, method)
    r = method(url, auth= auth, **kw)
    r.raise_for_status()
    return r.content


do_gh('https://api.github.com/user/keys', data=keyjson)
user = json_loads(do_gh('https://api.github.com/users/%s' % name, method='get'))

# print "run this on your client machine(s):"
os.system("git config --global user.email '%s'" % user['email'])
os.system("git config --global user.name '%s'" % user['name'])
# print "git clone %s" % fork['git_url']
# print "cd %s" % fork['name']
# print "git remote add course %s" % fork['source']['git_url']
