from flask import jsonify

from helpers.getters import Getters as getter
from helpers.putters import Putters as putter

def get(username):
	results = dict()

	user = getter.user(username)
	results['user'] = user
	return jsonify(results)


def post_history(_id, username):
	results = dict()

	
	user = putter.user_history(username, _id)
	return jsonify(results)