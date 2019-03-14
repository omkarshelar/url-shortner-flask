# This is app.py, this is the main file called.
from app import app
from flask import render_template, session

app.secret_key = 'any random string'


@app.route('/')
def index():
	if 'email' in session:
		return render_template('home.html', session = session)
	else:
		return render_template('home.html')
	

if __name__ == '__main__':
		app.run(debug=True)