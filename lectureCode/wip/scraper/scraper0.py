#!/usr/bin/env python
import re
import urllib2
from BeautifulSoup import BeautifulSoup

DOMAIN = "http://www.hampshire.edu"

mailhref = re.compile(r"^mailto\.php\?email=(.*)$")
namechunks = re.compile(r"^(.*), (.*?)(?: ([A-Z])\.)?$")

def open_soup(url):
    page = urllib2.urlopen(DOMAIN + url)
    return BeautifulSoup(page.read())

def next_page(soup):
    return soup.find(text="NEXT").parent.get("href")

soup = open_soup("/directory/results.php")
nxt = next_page(soup)

while soup is not None:
    # process page
    for mail_a in soup.findAll("a", href=mailhref):
        href = mail_a.get("href")
        user = mailhref.findall(href)[0]

        email = user + "@hampshire.edu"

        td = mail_a.parent
        fullname = td.find("font").string
        last, first, mi = namechunks.findall(fullname)[0]

        tr = td.parent
        role = tr.find("td").find(text=True).string

        if role.lower() == "student":
            print first, last, "<"+email+">,"

    # grab next page
    url = next_page(soup)
    if url is not None:
        soup = open_soup(url)
    else:
        soup = None

