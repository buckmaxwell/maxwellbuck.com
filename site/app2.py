from flask import Flask
from flask import request
from user_agents import parse


app = Flask(__name__)


def is_mobile(user_agent):
	user_agent = parse(user_agent)
	return user_agent.is_mobile or user_agent.is_tablet

def make_mobile(content):
	with open('mobile-header.html', "r") as f:
		header = f.read()

	# throw away desktop header
	content = content.split('</head>')[1]

	# add mobile header
	content = header + content

	return content

@app.route("/")
def hello():
	print "gete"
	with open("index.html", "r") as f:
		content = f.read()
		if is_mobile(request.headers.get('User-Agent')):
			content = make_mobile(content)

	return content

@app.route("/<filename>.html")
def hello2(filename):
	print "wee here"
	filename = filename + ".html"
	with open(filename, "r") as f:
		content = f.read()
		if is_mobile(request.headers.get('User-Agent')):
			content = make_mobile(content)
	return content


@app.route("/images/<filename>")
def hello3(filename):

	print "we hereee"
	with open("images/{}".format(filename), "r") as f:
		content = f.read()
	return content

@app.route("/<filename>")
def hello4(filename):
	filename = filename + ".css"
	print filename
	with open(filename, "r") as f:
		content = f.read()
	return content

if __name__ == "__main__":
    app.run(debug=True)