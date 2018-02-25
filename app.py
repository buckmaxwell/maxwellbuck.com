from flask import Flask
from flask import request
from user_agents import parse
from flask import render_template
from names import get_first_name as gfn
from names import get_last_name as gln
from random import randint as ri
from uuid import uuid4
import pytz
import datetime
import psycopg2
import urlparse
import os

app = Flask(__name__)

# Constants
COOKIE_NAME = 'ooh_so_tasty'
utc=pytz.UTC
FUTURE = 'Wed, 01 Jan 2116 20:43:10 GMT' # too far in future
#FUTURE = 'Fri, 01 Jan 2038 20:43:10 GMT' # hopefully not too far
#FUTURE = 'Mon, 13 Aug 2018 20:43:10 GMT' # one more try?

def get_connection():
    # create psycopg2 connection
    urlparse.uses_netloc.append("postgres")
    url = urlparse.urlparse(os.environ["DATABASE_URL"])
    conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )
    return conn


def is_mobile(user_agent):
	user_agent = parse(user_agent)
	return user_agent.is_mobile or user_agent.is_tablet


def get_username():
	name = gfn() + gfn() + gln() + gln()
	number = str(ri(1111, 9999))
	return name + number


def create_user(headers):
	"""Creates a user in the database and returns the username"""

	# Collect User Info
	id = str(uuid4())
	username = get_username()
	useragent = headers.get('User-Agent')
	mobile = is_mobile(useragent)
	ipaddr = headers.get('X-Forwarded-For', request.remote_addr)
	'''
	start_edit = utc.localize(datetime.datetime.utcnow()) +\
                         datetime.timedelta(seconds=time_to_wait)'''

	# Add User to DB
	conn = get_connection()
	cur = conn.cursor()
	cur.execute("INSERT INTO users (id, username, useragent, mobile, ipaddress) values (%s, %s, %s, %s, %s);",
	 (id, username, useragent, mobile, ipaddr))
	conn.commit()
	conn.close()

	# Return username
	return username



def create_event(headers, cookies, page):
	"""Create an event, creating a user if need one doesn't yet exist.
	Return a username if a new user was created.
	"""

	# Get connection
	conn = get_connection()
	cur = conn.cursor()

	created_user = False

	# See if user exists
	username = cookies.get(COOKIE_NAME)
	if username:
		# See if user exists (part 2)
		cur.execute("SELECT username from users WHERE username=%s", (username, ))
		try:
			username = cur.fetchone()[0]
		except:
			username = None

	# Create user if not
	if not username:
		username = create_user(headers)
		created_user = True

	# Collect event info
	id = str(uuid4())
	time = utc.localize(datetime.datetime.utcnow())
	referer = headers.get('Referer')

	# Add entry to events
	cur.execute("INSERT INTO events (id, page, username, time, referer) VALUES (%s, %s, %s, %s, %s)",
	 (id, page, username, time, referer))
	conn.commit()
	conn.close()

	# Return the username (if it's new)
	if created_user:
		return username
	else:
		return None


def return_404(mobile=False):
	with open("site/404.html", "r") as f:
		content = f.read()
		if mobile:
			content = make_mobile(content)
	return content, 404, {'Content-Type':'text/html'}

def make_mobile(content):
	with open('site/mobile-header.html', "r") as f:
		header = f.read()

	# throw away desktop header
	content = content.split('</head>')[1]

	# add mobile header
	content = header + content

	return content

@app.route("/")
def hello():
	try:
		with open("site/index.html", "r") as f:
			content = f.read()
			try:
				if is_mobile(request.headers.get('User-Agent')):
					content = make_mobile(content)
			except:
				pass
		#u = create_event(request.headers, request.cookies, 'index.html')
		headers = {'Content-Type':'text/html'}
		#if u:
		#	headers['Set-Cookie'] = "{}={}; Expires={};".format(COOKIE_NAME, u, FUTURE)
		return content, 200, headers
	except Exception as e:
		print e
		return return_404(is_mobile(request.headers.get('User-Agent')))


@app.route("/<filename>.html")
def hello2(filename):
	try:
		filename = filename + ".html"
		with open("site/{}".format(filename), "r") as f:
			content = f.read()
			if is_mobile(request.headers.get('User-Agent')):
				content = make_mobile(content)
		
		#u = create_event(request.headers, request.cookies, filename)
		headers = {'Content-Type':'text/html'}
		#if u:
		#	headers['Set-Cookie'] = "{}={}; Expires={};".format(COOKIE_NAME, u, FUTURE)
		return content, 200, headers
	except:
		return return_404(is_mobile(request.headers.get('User-Agent')))


@app.route("/images/<filename>")
def hello3(filename):
	try:
		with open("site/images/{}".format(filename), "r") as f:
			content = f.read()
		ext = filename.split('.')[1]

		#u = create_event(request.headers, request.cookies, filename)
		headers = {'Content-Type':'image/{}'.format(ext)}
		#if u:
		#	headers['Set-Cookie'] = "{}={}; Expires={};".format(COOKIE_NAME, u, FUTURE)
		return content, 200, headers
	except:
		return return_404(is_mobile(request.headers.get('User-Agent')))

@app.route("/site/asset/<filename>.css")
def site_asset(filename):
	try:
		filename = filename + ".css"
		with open("site/asset/{}".format(filename), "r") as f:
			content = f.read()

		#u = create_event(request.headers, request.cookies, filename)
		headers = {'Content-Type':'text/css'}
		#if u:
		#	headers['Set-Cookie'] = "{}={}; Expires={};".format(COOKIE_NAME, u, FUTURE)
		return content, 200, headers
	except:
		return return_404(is_mobile(request.headers.get('User-Agent')))


@app.route("/site/static/octicons/<filename>.css")
def static_octicons(filename):
	try:
		filename = filename + ".css"
		with open("site/static/octicons/{}".format(filename), "r") as f:
			content = f.read()

		#u = create_event(request.headers, request.cookies, filename)
		headers = {'Content-Type':'text/css'}
		#if u:
		#	headers['Set-Cookie'] = "{}={}; Expires={};".format(COOKIE_NAME, u, FUTURE)
		return content, 200, headers
	except:
		return return_404(is_mobile(request.headers.get('User-Agent')))



@app.route("/site/static/<filename>.<ext>")
def site_static(filename):
	try:
                filename = filename + '.' + ext
		with open("site/static/{}".format(filename), "r") as f:
			content = f.read()

		#u = create_event(request.headers, request.cookies, filename)
		#headers = {'Content-Type':'text/css'}
		#if u:
		#	headers['Set-Cookie'] = "{}={}; Expires={};".format(COOKIE_NAME, u, FUTURE)
		return content, 200, headers
	except:
		return return_404(is_mobile(request.headers.get('User-Agent')))

@app.route("/static/<filename>.<ext>")
def _static(filename):
        print "I AM HERE"
	try:
                filename+'.'+ext
		with open("site/static/{}".format(filename), "r") as f:
			content = f.read()

		#u = create_event(request.headers, request.cookies, filename)
		#headers = {'Content-Type':'text/css'}
		#if u:
		#	headers['Set-Cookie'] = "{}={}; Expires={};".format(COOKIE_NAME, u, FUTURE)
		return content, 200, headers
	except:
		return return_404(is_mobile(request.headers.get('User-Agent')))
######

@app.route("/<filename>.css")
def hello4(filename):
	try:
		filename = filename + ".css"
		with open("site/{}".format(filename), "r") as f:
			content = f.read()

		#u = create_event(request.headers, request.cookies, filename)
		headers = {'Content-Type':'text/css'}
		#if u:
		#	headers['Set-Cookie'] = "{}={}; Expires={};".format(COOKIE_NAME, u, FUTURE)
		return content, 200, headers
	except:
		return return_404(is_mobile(request.headers.get('User-Agent')))


@app.route("/<filename>.md")
def hello5(filename):
	try:
		filename = filename + ".md"
		with open("site/{}".format(filename), "r") as f:
			content = f.read()

		#u = create_event(request.headers, request.cookies, filename)
		headers = {'Content-Type':'text/plain'}
		#if u:
		#	headers['Set-Cookie'] = "{}={}; Expires={};".format(COOKIE_NAME, u, FUTURE)
		return content, 200, headers
	except:
		return return_404(is_mobile(request.headers.get('User-Agent')))


@app.route("/<filename>.pub")
def hello6(filename):
	try:
		filename = filename + ".pub"
		with open("site/{}".format(filename), "r") as f:
			content = f.read()

		#u = create_event(request.headers, request.cookies, filename)
		headers = {'Content-Type':"application/x-pem-file"}
		#if u:
		#	headers['Set-Cookie'] = "{}={}; Expires={};".format(COOKIE_NAME, u, FUTURE)
		return content, 200, headers
	except:
		return return_404(is_mobile(request.headers.get('User-Agent')))


@app.errorhandler(404)
def page_not_found(e):
	return return_404(is_mobile(request.headers.get('User-Agent')))

# caused by fake md, html, or image/* file
@app.errorhandler(500)
def page_not_found2(e):
	return return_404(is_mobile(request.headers.get('User-Agent')))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10200, debug=True)
