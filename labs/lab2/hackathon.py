import math
#Assume that you are ordering pizzas for a hackathon from a nearby pizza shop. Each pizza contains 8 slices. Similarly, you are also going to get some tubs of ice cream, such that each tub contains 24 scoops. 
#Write a program (hackathon.py) that calculates the number of pizzas and tubs of ice cream needed for a hackathon, with the minimum amount of leftovers. The program should ask the user for the number of people attending the hackathon, the number of pizza slices each person, and the number of ice cream scoops each person will be given. The program should display the following details

people = int (input("enter the number of people attending the party"))
print ("the number of people attending the party are", people)
slices = int (input("enter the number of slice of pizza each person would have?"))
pizza1 = (slices*people) /8
pizza2 = math.ceil(pizza1)
print ("the number of pizzas required is ", pizza2)
print ("the number of pizza slices leftover is", (pizza2*8) - (slices*people))
scoops = int (input("enter the number of scoops each person would have"))
icecreams = (people*scoops) /24
icecream1 = math.ceil(icecreams)
print ("the number of icecream tubs required is", icecream1)
print ("the number of scoops leftover is", (icecream1*24) - (people*scoops))


