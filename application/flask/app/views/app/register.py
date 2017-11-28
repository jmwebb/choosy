from helpers.putters import Putters as putter

def put(request):
	return putter.user(
		request.args.get('username'),
		request.args.get('first_name'),
		request.args.get('last_name'),
		request.args.get('email'),
		request.args.get('password'))