from flask import Blueprint

api = Blueprint('api', __name__)

@api.route('/test')
def index():
	return 'Hello World!'



# @app.route('/restaurants')
# def restaurants():
# 	restaurants.view()


# @app.route('/search?q=[args]')
# def search():
# 	search.view(args=args)


# @app.route('/login')
# def login():
# 	login.view()


# @app.route('/user/')
# def user():
# 	user.view('CREATE')


# @app.route('/user/[id]')
# def user():
# 	user.view(id)


# @app.route('/restaurants')
# def index():
# 	restaurants.view()