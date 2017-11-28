from helpers.getters import Getters as getter

def get(request):
	results = dict()

	user = getter.user(request.args.get('username'))
	results['user'] = user

	return results