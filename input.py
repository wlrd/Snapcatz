from bottle import get, post, request, run # or route

@get('/login') # or @route('/login')
def login():
    return '''
        <form name="input" action="/login" method="post">
		Username: 
		<input type="text" name="username">
		Password:
		<input type="password" name="password">
		<input type="submit" value="Submit">
		</form>
    	'''

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

def check_login(username, password):
	if (username in users and password == users[username]):
		return True
	else:
		return False

users = {"tlomont":"asdf1234"}

run(host='localhost', port= 8080, debug=True)