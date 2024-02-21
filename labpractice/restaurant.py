#You have a group of friends coming to visit for your high school reunion, and you want to take them out to eat at a local restaurant. You aren’t sure if any of them have dietary restrictions, but your restaurant choices are as follows
veg=str(input("are you a vegetarian?"))
vegan=str(input("are you a vegan?"))
gf=str(input("do you prefer gluten free?"))

if veg=="yes":
	if vegan=="yes":
		if gf=="yes":
			print("your restaurant choice is CORNER CAFE (or) THE CHEFS KITCHEN")

if veg=="no":
	if vegan=="no":
		if gf=="no":
			print("your restaurant choice is JOES GOURMET BURGERS")
if veg=="yes":
	if vegan=="no":
		if gf=="yes":
			print("your restaurant choice is MAIN STREET PIZZA COMPANY")
if veg=="yes":
	if vegan=="no":
		if gf=="no":
			print("your restaurant choice is MAMA'S FINE ITALIAN")
else:
	print("there is no restaurant that meets your requirement")
	print("you have to starve whole day")
