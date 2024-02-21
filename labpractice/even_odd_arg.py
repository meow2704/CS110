def is_even(n):

	if (n % 2) == 0:
		output = True
	else:
		output = False
	return output


def main():
	number=int(input("enter an integer: "))
	result = is_even(n)
	print (result)
main()