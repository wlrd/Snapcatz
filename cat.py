import re
import urllib2
from bs4 import BeautifulSoup
<<<<<<< HEAD
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
=======

from bottle import get, post, request, run
from snapchat import Snapchat
import getpass
import urllib

#TODO: change user agent string
hdr = { 'User-Agent' : 'super happy flair bot by /u/spladug' }



url = 'http://www.reddit.com/r/catpictures'
conn = urllib2.urlopen(urllib2.Request(url, headers=hdr))
html = conn.read()
soup = BeautifulSoup(html)
a = []
for elem in soup.findAll('a', href=re.compile('\.imgur\.com/')):
	a.append(elem['href'])
	#print a

url = 'http://www.reddit.com/r/catpictures/?count=25&after=t3_1u5r74'
conn = urllib2.urlopen(urllib2.Request(url, headers=hdr))
html = conn.read()
soup = BeautifulSoup(html)
#for elem in soup.findAll('a', href=re.compile('\.imgur\.com/')):
	#print elem['href']

url = 'http://www.reddit.com/r/catpictures/?count=75&after=t3_1u0dwn'
conn = urllib2.urlopen(urllib2.Request(url, headers=hdr))
html = conn.read()
soup = BeautifulSoup(html)
#for elem in soup.findAll('a', href=re.compile('\.imgur\.com/')):
	#print elem['href']


@get('/login')
def login():
	return '''
		<form name="input" action="/login" method="post">
		Your Username: 
		<input type="text" name="username">
		Password:
		<input type="password" name="password">
		Recipient Username:
		<input type="text" name="friend">
		<input type="submit" value="Submit">
		</form>
		'''

@post('/login')
def do_login():
	from random import choice
	url_final = choice(a)
	while("domain" in url_final):
		url_final = choice(a)
	print url_final
	name = request.forms.get('username')
	password = request.forms.get('password')
	friend = request.forms.get('friend')
	url = request.forms.get('pic_url')
	urllib.urlretrieve(url_final, "1.jpg")
	pic = "1.jpg"
	s = Snapchat()
	s.login(name, password)

	# Send a snapchat
	media_id = s.upload(Snapchat.MEDIA_IMAGE, pic)
	s.send(media_id, friend)

run(host='localhost', port=8080, debug=True)
>>>>>>> tommy

