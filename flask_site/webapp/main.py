from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/') # '/' is the root homepage
def index():
	return render_template("main.html")

'''
@app.route('/imageit', methods=['GET','POST']) # '/' is the root homepage
def imageit():
	if request.method == 'POST':
		return "You are using POST"
	elif request.method == 'GET':
		return "you are using GET"			


@app.route('/imageit')
def imageit():
	return "<h2>This is the imageit start</h2>"

@app.route('/team/<teammember>')
def team(teammember):
	return "<h2>Hello, my name is %s</h2>" % teammember

@app.route('/team/<int:memberid>')
def teammember(memberid):
	return "<h2>This members id is %s</h2>" % memberid
'''

if __name__ == "__main__":
	app.run(debug=True)