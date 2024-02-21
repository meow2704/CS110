veg=str(input("are you a vegetarian?"))
vegan=str(input("are you are a vegan?"))
gf=str(input("do you prefer gluten free food?"))
if veg=="yes":
	if vegan=="yes":
		if gf=="yes":
			print("your restaurant choice is CORNER CAFE OR THE CHEF'S KITCHEN")

		else:
			print("there is no restaurant of your choice")
	else:
		if gf=="yes":
			print("your restaurant choice is MAIN STREET PIZZA COMPANY")
		else:
			print("your restaurant choice is MAMA'S FINE ITALIAN")
else:
	if vegan=="no":
		if gf=="no":
			print("your restaurant choice is JOES GOURMET BURGERS")
		else:
			print("there is no restaurant of your choice")
	else:
		print("there is no restaurant of your choice")


