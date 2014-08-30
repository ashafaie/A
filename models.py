
from sqlalchemyinit import db

class User (db.Model):

	id = db.Column (db.Integer, primary_key=True)
	username = db.Column (db.String, unique=True, index=True)
	password = db.Column (db.String)

	def __repr__ (self):
		return self.username

