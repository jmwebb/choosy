from flask import jsonify

from helpers.getters import Getters as getter

def get():
	results = dict()
	categories = set()

	restaurants = getter.restaurants()
	for rest in restaurants:
		for cat in restaurants[rest]['categories']:

			categories.add(cat['alias'])

	results['categories'] = list(categories)

	return jsonify(results)