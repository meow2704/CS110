print("welcome to the Calculator program")
a=int(input("enter your first number"))
b=int(input("enter your second number"))
operator= input("enter which operator do you want to use + , - , / , * ")

def add(a,b):
	return a+b

def sub(a,b):
	return a-b

def multiply(a,b):
	return a*b

def divide(a,b):
	return a/b


if operator == '+':
	print(f"the final value of this math operation is {add(a,b)}")
elif operator == '-':
	print(f"the final value of this math operation is {sub(a,b)}")
elif operator == '*':
	print(f"the final value of this math operation is {multiply(a,b)}")
else:
	print(f"the final value of this math operation is {divide(a,b)}")