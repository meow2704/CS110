import random


persons = ["Ada Lovelace", "Grace Hopper", "Charles Babbage", "Alan Turing"]
places = ["Paris", "India", "China", "Tokyo"]
weathers = ["sunny", "rainy", "Cold", "calm"]
plurals1 = ["beaches", "mountains", "forests", "lakes", "stores"]
plurals2 = ["sandcastles", "good sceneries", "friends", "adventures"]


person = random.choice(persons)

place = random.choice(places)

weather = random.choice(weathers)

same_place = place

plural1 = random.choice(plurals1)

plural2 = random.choice(plurals2)

'''madlib = f"Last summer, we went for a vacation with", person, "on a trip to ", place,". The weather there is very ", weather,"! Northern ", same_place," has many ", plural1, ", and they make ", plural2, " there.")
'''
madlib_handler=open("madlib.txt", "w")
madlib_handler.write(f"Last summer, we went for a vacation with {person} on a trip to  {place}. The weather there is very {weather}! Northern {same_place} has many {plural1}, and they make {plural2} there.")
