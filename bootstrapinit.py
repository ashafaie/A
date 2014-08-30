
from appinit import app

from flask.ext.bootstrap import Bootstrap

app.config ['SECRET_KEY'] = "KEY"

bootstrap = Bootstrap (app)

