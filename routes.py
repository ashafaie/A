
from blueprints.index import *
from blueprints.user import *
from appinit import app
from bootstrapinit import bootstrap
from sqlalchemyinit import *
from forms import RegisterationForm, LoginForm
from models import User

from flask import session, g, render_template, url_for, redirect
from werkzeug.security import generate_password_hash, check_password_hash

app.register_blueprint (index_blueprint)
app.register_blueprint (user_blueprint)

