#!/usr/bin/python

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html',name=name)

@app.route('/')
def index():
	return '<h1>Welcome Home Page</h1>'

@app.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'POST':
		do_the_login()
	else:
		show_the_login_from()
@app.route('/user/<name>')
def user(name):
	return render_template('user.html',user=name)

@app.route('/post/<int:post_id>')
def show_post(post_id):
	return 'Post %d ' % post_id

@app.route('/projects/')
def projects():
	return 'The project page'

@app.route('/about')
def about():
	return 'The about page'

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')
