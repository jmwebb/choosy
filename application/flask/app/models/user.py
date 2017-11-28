class User():

	def __init__(self, _id, is_authenticated=True, is_active=True, is_anonymous=False):
		self.id = _id
		self.is_authenticated = is_authenticated
		self.is_active = is_active
		self.is_anonymous = is_anonymous

	def get_id(self):
		return self.id