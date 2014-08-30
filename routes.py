
from appinit import app
from bootstrapinit import bootstrap
from sqlalchemyinit import *
from forms import RegisterationForm, LoginForm
from models import User

from flask import session, g, render_template, url_for, redirect
from werkzeug.security import generate_password_hash, check_password_hash

@app.route ('/')
def index ():
	return render_template ('index.html')

@app.route ('/user/login', methods=['GET','POST'])
def login ():
	loginform = LoginForm ()

	if loginform.validate_on_submit():
		if (check_password_hash (User.query.filter_by
								(username=loginform.username.data).first().password,
														loginform.password.data)):
			session['username'] = loginform.username.data
			return redirect (url_for('index'))

	return render_template ('login.html',login_form=loginform)

@app.route ('/user/register', methods=['GET','POST'])
def register ():
	registerform = RegisterationForm ()

	if registerform.validate_on_submit():
		new_user = User (username=registerform.username.data,
					password=generate_password_hash (registerform.password.data))
		db.session.add (new_user)
		db.session.commit ()
		session['username'] = new_user.username
		return redirect (url_for('index'))
		
	return render_template ('register.html', registeration_form = registerform) 

@app.route ('/user/logout', methods=['GET'])
def logout ():
	session['username'] = None
	return redirect (url_for('index'))

