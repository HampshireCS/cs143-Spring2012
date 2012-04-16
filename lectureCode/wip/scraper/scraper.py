import re
import urllib2
from BeautifulSoup import BeautifulSoup

url = "http://www.hampshire.edu/directory/results.php"
DOMAIN = "http://www.hampshire.edu"

anything = re.compile(r".*")
mailhref = re.compile("^mailto.php\?email=(.*)$")
namechunks = re.compile(r"^(.*), (.*?) ?([A-Z])?\.?$")

class Person(object):
    def __init__(self, first, last, mi, email, role):
        self.first = first
        self.last = last
        self.mi = mi
        self.email = email
        self.role = role

class PageScraper(object):
    def __init__(self, url):
        page = urllib2.urlopen(url)
        self.soup = BeautifulSoup(page.read())
        page.close()

    def get_next(self):
        tag = self.soup.find(text="NEXT").parent # get the a tag containing next
        if tag.name.lower() == "a":
            return PageScraper(DOMAIN + tag.get("href").strip())
        else:
            return None

    def get_people(self):
        people = []

        # get every link
        for mail_a in self.soup.findAll("a", href=mailhref):
            # extract email address
            href = mail_a.get("href")
            user = mailhref.findall(href)[0]
            email = user + "@hampshire.edu"

            # extract name
            td = mail_a.parent
            fullname = td.find("font").string
            last, first, mi = namechunks.findall(fullname)[0]


            # get role (aka type)
            row = td.parent
            role = row.find("td").find(text=True)

            # create a new person
            people.append(Person(first, last, mi, email, role))

        return people

# open site
page = PageScraper(url)

# loop through all pages
people = []
while page is not None:
    people += page.get_people()
    page = page.get_next()

print len(people)
