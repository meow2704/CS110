minsteps=10000
steps=int(input("enter the number of steps you walked today"))
while steps<minsteps:
	print("you have not walked enough today please try again")
	print("enter the new step total")
	steps=int(input("enter the  updated number of steps you walked today"))
print(f"you have completed the steps requirement {steps}")