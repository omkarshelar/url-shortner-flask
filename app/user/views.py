from flask import Blueprint,render_template,redirect,url_for, abort
from app.user.forms import SignupForm, LoginForm
import bcrypt
from app.user.models import add_user, load_user
from flask import session, flash

users_blueprint = Blueprint('user',
															__name__,
															template_folder='templates/user')

@users_blueprint.route('/signup/', methods=['GET', 'POST'])
def signup():
	form = SignupForm()
	print(form.validate_on_submit())
	if form.validate_on_submit():
		print(form.email.data)
		name = form.name.data
		email = form.email.data
		password = form.password.data
		password1 = form.password_conf.data
		if password != password1:
			return '<h1>Password do not match!</h1>'
		hashed_pwd = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
		if bcrypt.checkpw(password.encode('utf8'), hashed_pwd):
			res = add_user(email, hashed_pwd, name)
		if res:
			session['email'] = email
			session['name'] = name
			return redirect(url_for('index'))
		else:
			return redirect(url_for('user.login'))

	return render_template('signup.html',form=form)

@users_blueprint.route('/login/', methods=['GET', 'POST'])
def login():
		form = LoginForm()

		if form.validate_on_submit():
			email = form.email.data
			password = form.password.data
			user_email, user_pwd_hash, user_name = load_user(email)
			if user_email is None:
				flash('User not present')
			elif not bcrypt.checkpw(password.encode('utf8'), user_pwd_hash):
				flash('Incorrect Password!')
				return redirect(url_for('user.login'))
			else:
				session['email'] = user_email
				session['name'] = user_name
			return redirect(url_for('index'))
			
		return render_template('login.html',form=form)

@users_blueprint.route('/logout/', methods=['GET'])
def logout():
	session.pop('email', None)
	session.pop('name', None)
	return redirect(url_for('index'))
