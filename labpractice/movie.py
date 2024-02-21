#omyaasree balaji
#cs 110
#in class :Introduction to Classes & Objects
class Movie:
	def __init__(self, title, releasedate, rating, director):
		self.__title = title
		self.__releasedate = releasedate
		self.__rating = rating
		self.__director = director

	def set_title ( self, title):
		self.__title = title

	def set_releasedate (self, releasedate):
		self.__releasedate = releasedate

	def set_rating(self, rating):
		self.__rating = rating

	def set_director (self, director):
		self.__director = director

	def get_title (self):
		return self.__title

	def get_releasedate (self):
		return self.__releasedate

	def get_rating (self):
		return self.__rating

	def get_director (self):
		return self.__director

	def __str__(self):
		return f'{self.__title} is the name of the movie air on {self.__releasedate}, has a rating of {self.__rating} and was directed by {self.__director}'