

from flask import Flask, render_template, url_for, redirect, make_response
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask (__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config ['SECRET_KEY'] = "KEY"
app.config['SQLALCHEMY_DATABASE_URI'] =\
					'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)
bootstrap = Bootstrap (app)

