from flask import jsonify
from flask import render_template
import operator
import random

from helpers.getters import Getters as getter

MIN_OPTIONS = 3


def next_question(remaining, exclude, is_first_question):
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
		if is_first_question:
			rand_alias = random.choice(alias_to_category.keys())
			return alias_to_category[rand_alias]
		max_alias = max(category_count.iteritems(), key=operator.itemgetter(1))[0]
		return alias_to_category[max_alias]
	return None


def search(request, username):
	results = dict()

	user = getter.user(username)
	

	user_history = list()
	for restaurant_id in user.get('history', [])[::-1]:
		user_history.append(getter.restaurant(restaurant_id))

	user['history'] = user_history

	results['user'] = user

	category_filters = dict()

	for key in request.args:
		category_filters[key] = bool(int(request.args.get(key)))

	results['is_first_question'] = int(len(category_filters) == 0)

	restaurants = getter.restaurants(category_filters)

	results['next_question'] = next_question(restaurants, category_filters, results['is_first_question'])
	
	if len(restaurants) <= MIN_OPTIONS:
		results['next_question'] = None


	results['restaurants'] = restaurants

	return render_template('search.html',results=results)
	# return jsonify(results)