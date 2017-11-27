from flask import abort
from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask_login import login_required
from flask_login import login_user

from app.forms.login_form import LoginForm
from app.views.app import search as app_search

# Blueprint specifies name of route for access by run.py
# Also specifies resource locations
# e.g. templates are found in 
# <path to choosy>/application/flask/app/templates
application = Blueprint('application', __name__
	,template_folder='../templates')


@application.route('/')
@login_required
def index():
	return 'Hello World!'

@application.route('/login', methods=['GET', 'POST'])
def login():
	# Here we use a class of some kind to represent and validate our
	# client-side form data. For example, WTForms is a library that will
	# handle this for us, and we use a custom LoginForm to validate.
	form = LoginForm(request.form)
	if form.validate_on_submit():
		# Login and validate the user.
		# user should be an instance of your `User` class
		# form.
		login_user(user)

		flash('Logged in successfully.')

		next = request.args.get('next')
		# is_safe_url should check if the url is safe for redirects.
		# See http://flask.pocoo.org/snippets/62/ for an example.
		if not is_safe_url(next):
			return abort(400)

		return redirect(next or flask.url_for('index'))
	return render_template('login.html', form=form)


@application.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect('/login')


@application.route('/search', methods=['GET'])
def search():
	return app_search.search(request)
