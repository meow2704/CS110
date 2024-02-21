import random
print("Welcome to Rock Paper Scissor game")
print("1=rock, 2=paper, 3=scissor ")
rps=int(input('enter a value from 1, 2 and 3 : '))

choice='y'
while choice=='y':

	while rps < 1 or rps > 3:
		print("out of bound exception")
		rps = int(input("enter your choice: "))

	random_rps = random.randint(1,3)

	if random_rps == 1:
		print("the computer chose rock")
	if random_rps == 2:
		print("the computer chose paper")
	if random_rps == 3:
		print("the computer chose scissor")

	if rps == 1:
		print('you chose rock')
	elif rps == 2:
		print('you chose paper')
	else:
		print ("you chose scissor")

	if random_rps == rps:
		print('its a Tie try again')
	elif random_rps == 1 and rps == 2:
		print('yay!! you WON,')
	elif random_rps == 2 and rps == 3:
		print('yay!! you WON,')
	elif random_rps == 3 and rps == 1:
		print('yay!! you WON,')
	elif random_rps == 1 and rps == 3:
		print('the computer wins, better luck next time')
	elif random_rps == 3 and rps == 2:
		print('the computer wins, better luck next time')
	else:
		print('the computer wins, better luck next time')


	while (True):
		choice=str(input("do you want to continue? enter y for yes and n for no: "))
		if choice=="y":
			print("Welcome to Rock Paper Scissor game")
			print("1=rock, 2=paper, 3=scissor ")
			rps = int(input("enter your choice "))
			break
		elif choice=="n":
			print("thank you for playing with us")
			break
		else:
			print("please enter only y/n")


