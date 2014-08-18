
from appfile import *

from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required

class RegisterationForm (Form):

	username = StringField ('Username: ', validators=[Required()])
	password = PasswordField ('Password: ', validators=[Required()])
	submit = SubmitField ('Register')

