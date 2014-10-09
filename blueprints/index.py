
from flask import Blueprint, render_template

index_blueprint = Blueprint('index',__name__)

@index_blueprint.route ('/', methods=['GET','POST'])
def index ():
	return render_template ('index.html')

