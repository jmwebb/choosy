#!flask/bin/python
from firebase import firebase
from flask import Flask
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

from app.routes.api import api
from app.routes.application import application

# Load the Flask app
app = Flask(__name__)
firebase = firebase.FirebaseApplication('https://projectfor551.firebaseio.com/', None)

# Register blueprints, which contain the
# routes for this application
app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(application)

# Load login manager
login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
	return User.get(user_id)

# Set login view
login_manager.login_view = '/login'

# Set secret key
app.secret_key = 'super secret key'

# Set slash strictness
app.url_map.strict_slashes = False

csrf = CSRFProtect(app)
def create_app():
    app = Flask(__name__)
    csrf.init_app(app)


if __name__ == '__main__':
	app.run(debug=True)