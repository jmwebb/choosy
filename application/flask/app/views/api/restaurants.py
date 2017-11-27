from flask import jsonify

from helpers.getters import Getters as getter

def get(request):
	results = dict()

	category_filters = dict()

	for key in request.args:
		category_filters[key] = bool(int(request.args.get(key)))

	restaurants = getter.restaurants(category_filters)
	results['restaurants'] = restaurants

	return jsonify(results)