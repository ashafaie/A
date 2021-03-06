
from appinit import app
from bootstrapinit import bootstrap
from sqlalchemyinit import *
from forms import RegisterationForm, LoginForm
from models import User

from flask import Blueprint, session, g, render_template, url_for, redirect
from werkzeug.security import generate_password_hash, check_password_hash

user_blueprint = Blueprint('user',__name__)

@user_blueprint.route ('/login', methods=['GET','POST'])
def login ():
	loginform = LoginForm ()

	if loginform.validate_on_submit():
		if (User.query.filter_by(username=loginform.username.data).first()==None):
			return render_template ('login.html', correct=False,
												login_form = loginform)
		elif (check_password_hash (User.query.filter_by
                                                            (username=loginform.username.data).first().password,
                                                                                                        loginform.password.data)):
			session['username'] = loginform.username.data
			return redirect (url_for('index.index'))
		else:
			return render_template ('login.html', correct = False,
														login_form = loginform)

	return render_template ('login.html', correct = True, login_form = loginform)

@user_blueprint.route ('/register', methods=['GET','POST'])
def register ():
	registerform = RegisterationForm ()

	if registerform.validate_on_submit():
		if not User.query.filter_by(username=registerform.username.data).first()\
																			==None:
			return render_template ('register.html', duplicate = True,
										registeration_form = registerform)
		new_user = User (username=registerform.username.data,
					password=generate_password_hash (registerform.password.data))

		db.session.add (new_user)
		db.session.commit ()
		session['username'] = new_user.username
		return redirect (url_for('index.index'))
		
	return render_template ('register.html', duplicate = False,
											registeration_form = registerform) 

@user_blueprint.route ('/logout', methods=['GET'])
def logout ():
	session['username'] = None
	return redirect (url_for('index.index'))

