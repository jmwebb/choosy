from firebase import firebase
from flask import Blueprint
from flask import jsonify
from flask import request
import json

from app.views.api import categories as api_categories
from app.views.api import restaurants as api_restaurants

api = Blueprint('api', __name__, url_prefix='/api')


# @api.route('/restaurant', methods=['GET', 'POST'])
# def restaurant():
# 	return api_view.restaurant()

###############################################################################
#																			  #
#																			  #
#																			  #
###############################################################################

@api.route('/categories', methods=['GET'])
def categories():
	return api_categories.get()


@api.route('/restaurants', methods=['GET'])
def restaurants():
	return api_restaurants.get(request)



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