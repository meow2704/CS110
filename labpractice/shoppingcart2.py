print ("WELCOME TO HEALTHY FRUITS SHOP")
rasp = float(input("enter the number of pounds of raspberries would you like to have($1.75 per pound)"))
straw = float(input("enter the number of pounds of strawberries you would like to have($1.25 per pound)"))
cost = (rasp*1.75) + (straw*1.25)
print  ("the total cost of your purchase is $", cost)

cost1 = float(input("enter the amount you would like to pay"))
due1 = cost-cost1
while cost >= cost1:
	print (f"the amount due to the shop is {due1}")
	break
print(f"the amount due from the shop is {-due1}")
