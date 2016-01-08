#!/usr/bin/python

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/user/<name>')
def user(name):
	return render_template('user.html',user=name)

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')
