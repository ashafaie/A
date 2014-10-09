
from managerinit import manager
from routes import *
from models import User

from flask import session
from flask.ext.migrate import Migrate, MigrateCommand

@app.before_request
def before_request():
    if (session.__contains__('username')):
        g.user = User.query.filter_by (username=session['username']).first()

if __name__ == '__main__':
	migrate = Migrate(app, db)
	manager.add_command('db', MigrateCommand)
	db.create_all()
        app.run (debug=True)
	manager.run ()

