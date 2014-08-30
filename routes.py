
from appfile import app
from forms import *

@app.route ('/')
def index ():
	return render_template ('index.html')

@app.route ('/user/login', methods=['GET','POST'])
def login ():
	return render_template ('login.html')

@app.route ('/user/register', methods=['GET','POST'])
def register ():
	registerform = RegisterationForm ()
	return render_template ('register.html', registeration_form = registerform)

