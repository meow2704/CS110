print("WELCOME TO HEALTHY FRUITS SHOP")
rasp=float(input("enter the number of pounds of raspberries would you like to have($1.75 per pound)"))
straw=float(input("enter the number of pounds of strawberries you would like to have($1.25 per pound)"))
apple=int(input("enter the number of apples you would like to have($0.5 per apple)"))
mango=int(input("enter the number of mangoes you would like to have($1.75 per mango)"))
cost=(rasp*1.75)+(straw*1.25)+(apple*0.5)+(mango*1.75)
print("the total cost of your purchase is $", cost)
cost1=float(input("enter the amount you would like to pay"))
due1=cost1-cost
due=due1
if cost1>=cost:
	print(f"the amount due by the shop is {due}")

	num5=int(due//5)
	due=due-num5*5

	num1=int(due//1)
	due=due-num1*1

	quarters=int(due//0.25)
	due=due-quarters*0.25

	dimes=int(due//0.1)
	due=due-dimes*0.1

	nickels=int(due//0.05)
	due=due-nickels*0.05

	pennies=int(due*100)

	print(f"the change due is{due1}.give the customers {num5}$5notes, {num1}$1notes, {quarters}quarters, {dimes}dimes, {nickels}nickels, {pennies}pennies")
else:
	print("insufficiant funds")

