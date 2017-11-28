from firebase import firebase

firebase = firebase.FirebaseApplication('https://projectfor551.firebaseio.com/', None)

class Getters():

	@classmethod
	def _extract_aliases(scope, restaurant):
		alias_list = list()
		for category in restaurant.get('categories'):
			alias_list.append(category.get('alias'))
		return alias_list

	@classmethod
	def restaurant(scope, _id):
		response = firebase.get('/restaurants/' + '\"' + _id + '\"', None)
		return response


	@classmethod
	def restaurants(scope, category_filters):
		response = firebase.get('/restaurants', None)
		results = dict()
		for _id in response:
			restaurant = response.get(_id)
			alias_list = scope._extract_aliases(restaurant)
			if scope._passes_filters(alias_list, category_filters):
				results[_id] = restaurant

		return results


	@classmethod
	def user(scope, _id):
		response = firebase.get('/users/' + _id, None)
		return response


	@classmethod
	def _passes_filters(scope, alias_list, category_filters):
		_pass = True
		for category, should_include in category_filters.iteritems():
			included = category in alias_list
			if (included and not should_include) or (not included and should_include):
				_pass = False
		return _pass

