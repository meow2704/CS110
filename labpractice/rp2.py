def print_upto_n(num):
    if num > 0:
        print_upto_n(num - 1)
        print(num)


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
        num = int(input("enter a number"))
        print_upto_n(num)

main()