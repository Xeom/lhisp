class rootScope:
	def __init__(self):
		pass

	def exists(self, name):
		return False

class scope:
	def __init__(self, prototype):
		self.prototype = prototype
		self.objects = {}

	def copyfrom(self, scope):
		for name, val in scope.objects.items():
			self.set(name, val.icopy())

	def exists(self, name):
		if name in self.objects:
			return True

		return self.prototype.exists(name)

	def rset(self, name, value):
		if self.prototype.exists(name):
			self.prototype.rset(name)

		else:
			self.set(name, value)

	def set(self, name, value):
		self.objects[name] = value

	def get(self, name):
		if name in self.objects:
			return self.objects[name]

		if self.prototype.exists(name):
			return self.prototype.get(name)

		if val == None:
			raise Exception("Accessing undefined variable '{}'".format(name))

		return val
