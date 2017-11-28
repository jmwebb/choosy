from firebase import firebase

from helpers.getters import Getters as getter

firebase = firebase.FirebaseApplication('https://projectfor551.firebaseio.com/', None)

class Putters():

	@classmethod
	def user(scope, username, f_name, l_name, email, password):
		user_data = {
			'username': username,
			'first_name': f_name,
			'last_name': l_name,
			'email': email,
			'password': password,
			'history': []
		}
		return firebase.put('/users', username, user_data)


	@classmethod
	def user_history(scope, username, _id):
		user = getter.user(username)
		if user.get('history'):
			if _id in user['history']:
				user['history'].pop(user['history'].index(_id))
			user['history'].append(_id)
		else:
			user['history'] = [_id]
		user_data = {
			'username': user.get('username'),
			'first_name': user.get('first_name'),
			'last_name': user.get('last_name'),
			'email': user.get('email'),
			'password': user.get('password'),
			'history': user.get('history')
		}
		return firebase.put('/users', username, user_data)