
from routes import *

@app.before_request
def before_request():
	g.user = User.query.filter_by(username=session['username']).first()

if __name__ == '__main__':
	db.drop_all ()
	db.create_all ()
	app.run (debug=True)

