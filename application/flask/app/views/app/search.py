from flask import jsonify
from flask import render_template
import operator

from helpers.getters import Getters as getter

MIN_OPTIONS = 3


def next_question(remaining, exclude):
	alias_to_category = dict()

	category_count = dict()
	for _id in remaining:
		restaurant = remaining[_id]
		for category in restaurant.get('categories'):
			alias = category.get('alias')
			if exclude.get(alias):
				continue
			if not category_count.get(alias):
				alias_to_category[alias] = category
				category_count[alias] = 0
			category_count[alias] += 1
	if category_count:
		max_alias = max(category_count.iteritems(), key=operator.itemgetter(1))[0]
		return alias_to_category[max_alias]
	return None


def search(request):
	results = dict()

	category_filters = dict()

	for key in request.args:
		category_filters[key] = bool(int(request.args.get(key)))

	restaurants = getter.restaurants(category_filters)

	results['next_question'] = next_question(restaurants, category_filters)
	
	if len(restaurants) <= MIN_OPTIONS:
		results['next_question'] = None


	results['restaurants'] = restaurants

	return render_template('search.html',results=results)
	# return jsonify(results)