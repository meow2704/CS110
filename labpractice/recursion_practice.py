
def print_upto_n(num):
	num = int(input("Enter a number: "))
	if num > 0:
		print_upto_n(num - 1)
		print(num, end=' ')


def rec_mul(x, y):
	x = int(input("Enter the first number: "))
	y = int(input("Enter the second number: "))
	if y == 1:
		return x
	else:
		return x+ rec_mul(x, y - 1)


# def rec_n_asterisks(n):
#     if n > 0:
#         rec_n_asterisks(n - 1)
#         print('*' * n)

# def largest_in_list(input_list):
#     if len(input_list) == 1:
#         return input_list[0]
#     else:
#         rest_max = largest_in_list(input_list[1:])
#         return input_list[0] if input_list[0] > rest_max else rest_max

# def rec_list_sum(input_list):
#     if not input_list:
#         return 0
#     else:
#         return input_list[0] + rec_list_sum(input_list[1:])

# def rec_sum_to_n(num):
#     if num == 1:
#         return 1
#     else:
#         return num + rec_sum_to_n(num - 1)

# def rec_power(num, exponent):
#     if exponent == 0:
#         return 1
#     else:
#         return num * power(num, exponent - 1)



def main():

	print("select a function")
	print("1. Recursive Printing")
	print("2. Recursive Multiplication")
	print("3. Recursive Lines")
	print("4. Largest List Item")
	print("5. Recursive List Sum")
	print("6. Sum of Numbers")
	choice = str(input("Enter the choice (1-6): "))

	if choice == 1:
		print_upto_n(num)
	elif choice == 2:
		result = rec_mul(x, y)
    #     print(f"The result of {x} * {y} is: {result}")
    # elif choice == 3:
    #     n = int(input("Enter the number of lines: "))
    #     rec_n_asterisks(n)
    # elif choice == 4:
    #     input_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
    #     max_item = largest_in_list(input_list)
    #     print(f"The largest item in the list is: {max_item}")
    # elif choice == 5:
    #     input_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
    #     list_sum = rec_list_sum(input_list)
    #     print(f"The sum of the numbers in the list is: {list_sum}")
    # elif choice == 6:
    #     num = int(input("Enter a number: "))
    #     result = rec_sum_to_n(num)
    #     print(f"The sum of numbers from 1 to {num} is: {result}")

    # elif choice == 7:
    # 	num = float(input("Enter the base (num): "))
    # 	exponent = int(input("Enter the exponent: "))
    
    # 	result = power(num, exponent)
    # 	print(f"{num} raised to the power of {exponent} is: {result}")
    # else:
    	# print("invalid choice")

if __name__ == "__main__":
    main()
