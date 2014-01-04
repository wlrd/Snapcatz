import re
import urllib2
from bs4 import BeautifulSoup

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
for elem in soup.findAll('a', href=re.compile('\.imgur\.com/[a-zA-Z0-9]')):
	a.append(elem['href'])
	#print a

url = 'http://www.reddit.com/r/catpictures/?count=25&after=t3_1u5r74'
conn = urllib2.urlopen(urllib2.Request(url, headers=hdr))
html = conn.read()
soup = BeautifulSoup(html)
for elem in soup.findAll('a', href=re.compile('\.imgur\.com/[a-zA-Z0-9]')):
	a.append(elem['href'])
	#print elem['href']

url = 'http://www.reddit.com/r/catpictures/?count=75&after=t3_1u0dwn'
conn = urllib2.urlopen(urllib2.Request(url, headers=hdr))
html = conn.read()
soup = BeautifulSoup(html)
for elem in soup.findAll('a', href=re.compile('\.imgur\.com/[a-zA-Z0-9]')):
	a.append(elem['href'])
	#print elem['href']

a = list(set(a))

@get('/login')
def login():
	return '''
		<html>
		<head>
		<title> Snapcatz </title>
		<style type="text/css">
		body{
			font-family: 'Tahoma'
		}
		</style>
		</head>
		<div style="margin:20px auto; text-align:center; width:400px; height: 260px; border:2px solid; border-radius:20px; background-color: lightgray">
		<h1> Snapcatz!</h1>
		<p><form name="input" action="/login" method="post">
		Your Username: 
		<input type="text" name="username" style="border: 2px solid rgb(139, 188, 190); border-radius:5px"></p>
		<p>
		Password:
		<input type="password" name="password" style="border: 2px solid rgb(139, 188, 190); border-radius:5px"></p>
		<p>
		Recipient Username:
		<input type="text" name="friend" style="border: 2px solid rgb(139, 188, 190); border-radius:5px"></p>
		<p>
		<input type="submit" value="Submit"></p>
		</form>
		</div>
		<html>
		'''

@post('/login')
def do_login():
	from random import choice
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
