def is_even():
	number=int(input("enter an integer"))

	if (number % 2) == 0:
		print("the given number is an even number")
	else:
		print("the given number is an odd number")

def main():
	is_even()
main()