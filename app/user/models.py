import sqlite3, os
from flask import flash

cwd = os.getcwd()
db_path = os.path.join(cwd, 'app', 'url-shortner.sqlite3')

def add_user(email, password_hash, name):
	received_email = load_user(email)
	if received_email[0] is not None:
		flash('User already present. Please Login')
		return 0
	try:
		conn = sqlite3.connect(db_path)
		c = conn.cursor()
		params = (name, email, password_hash)
		c.execute('''
						INSERT INTO users(name, email, hashed_password) VALUES(?,?,?) 
						''', params)

		conn.commit()
		conn.close()
		return 1
	except Exception as e:
		print("Error Occurred!")
		print(e)
		return 0

def load_user(email):
	try:
		conn = sqlite3.connect(db_path)
		c = conn.cursor()
		params = (email,)
		res = c.execute('SELECT * FROM users WHERE email=?', params)
		if res:
			res = c.fetchone()
		if len(res) >= 1:
			return res[2], res[3], res[1]
	except:
		return None, None, None