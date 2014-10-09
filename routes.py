
from blueprints.index import *
from blueprints.user import *

app.register_blueprint (index_blueprint)
app.register_blueprint (user_blueprint,url_prefix='/user')

