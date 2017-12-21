

class User:
	"""Container class which encapsulates secret and private id """
	def __init__(self,p_id,secret):
		self.__secret = secret
		self.__pid = p_id

	@property
	def pid(self):
		return self.__pid

	@pid.getter
	def pid(self,pid):
		return self.__pid

	@property
	def secret(self):
		return self.__secret

	@secret.getter
	def secret(self):
		return self.__secret
	
