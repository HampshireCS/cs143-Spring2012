import requests
import json
import getpass

REPO_NAME = "bootstrap"
REPO_ORG = "twitter"

#REPO_NAME = "cs112-Spring2012"
#REPO_ORG = "HampshireCS112"

def do_gh(url, method="post", **kw):
    method = getattr(requests, method)
    r = method(url, **kw)
    r.raise_for_status()
    return r.content

fork_data = json.loads(requests.get('https://api.github.com/repos/%s/%s/forks' % (REPO_ORG, REPO_NAME).content)

urls = [{"url": x['git_url'],"username": x['owner']['login'] } for x in fork_data]

for d in urls:
    os.system("git clone %s %s" % (d['url'], d['username']))