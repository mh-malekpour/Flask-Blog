from flask import Blueprint

from . import views

blog = Blueprint('blog', __name__, url_prefix='/blog/')
