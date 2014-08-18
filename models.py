
from appfile import *

class User (db.Model):

	id = db.Column (db.Integer, primary_key=True)
	username = db.Column (db.StringText, unique=True, index=True)
	password = db.Column (db.StringText)

