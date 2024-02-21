class Dog:
	def __init__(self, name, birthdate, breed, color):
		self.__name = name
		self.__birthdate = birthdate
		self.__breed = breed
		self.__color = color

	def set_name (self, name):
		self.__name = name

	def set_birthdate (self, birthdate):
		self.__birthdate = birthdate

	def set_breed(self, breed):
		self.__breed = breed

	def set_color (self, color):
		self.__color = color

	def get_name (self):
		return self.__name

	def get_birthdate (self):
		return self.__birthdate

	def get_breed (self):
		return self.__breed

	def get_color (self):
		return self.__color

	def display_info(self):
		return f'{self.__name} was born on {self.__birthdate}, is a {self.__breed} and is of color by {self.__color}\n'