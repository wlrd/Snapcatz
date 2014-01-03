import re
import urllib2
from bs4 import BeautifulSoup
url = 'http://www.reddit.com/r/catpictures'
conn = urllib2.urlopen(url)
html = conn.read()
soup = BeautifulSoup(html)
for elem in soup.findAll('a', href=re.compile('\.imgur\.com/')):
    print elem['href']

url = 'http://www.reddit.com/r/catpictures/?count=25&after=t3_1u5r74'
conn = urllib2.urlopen(url)
html = conn.read()
soup = BeautifulSoup(html)
for elem in soup.findAll('a', href=re.compile('\.imgur\.com/')):
    print elem['href']

url = 'http://www.reddit.com/r/catpictures/?count=75&after=t3_1u0dwn'
conn = urllib2.urlopen(url)
html = conn.read()
soup = BeautifulSoup(html)
for elem in soup.findAll('a', href=re.compile('\.imgur\.com/')):
    print elem['href']

