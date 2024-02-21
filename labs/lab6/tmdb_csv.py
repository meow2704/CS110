#Omyaasree
#cs110
#lab6- Dictionaries, Sets, and APIs
#part 2


import csv 
import tmdbsimple as tmdb


tmdb.API_KEY = "2528c5ee8dd6917c833643e6b6c7fc1e"

while True:
	user_input = str(input("\nwhich movie do you want to search for :\n"))

	search = tmdb.Search()
	response = search.movie(query = user_input)

	for s in search.results:
		print(s['title'],  s['id'],  s['release_date'],  s['popularity'])


	with open('movie_results.csv', mode='w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(['title','ids','popularity','release_date'])
		for s in search.results:
			writer.writerow([s['title'],  s['id'], s['popularity'], s['release_date']])
	print("Inventory has been saved movie_results.csv")