def main():
    numbers = []

    while True:
        user_input = input("Enter a number (-1 to exit): ")

        if user_input == "-1":
            break
        if user_input.isdigit():
            num = int(user_input)
            numbers.append(num)

    largest = max(numbers)
    smallest = min(numbers)

    print(f"Largest number : {largest}")
    print(f"Smallest number : {smallest}")
    print(numbers)
main()
