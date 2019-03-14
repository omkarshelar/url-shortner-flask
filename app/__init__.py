import os
from flask import Flask
app = Flask(__name__)

# Often people will also separate these into a separate config.py file 
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))

from app.user.views import users_blueprint
# from myproject.owners.views import owners_blueprint

app.register_blueprint(users_blueprint,url_prefix="/user")
#app.register_blueprint(puppies_blueprint,url_prefix='/file')