from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World!'

@app.route('/banjo')
def banjo():
	return 'I like <a href="https://banjohangout.org">banjos</a>'