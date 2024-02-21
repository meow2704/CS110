user_input = int(input("Enter a positive integer: "))

#defining a function that displays all the prime numbers
def list_primes(n):

    for number in range(1, n + 1):
        if is_prime(number):
            print(number)

#defining a function of prime numbers
def is_prime(n):

    if n <= 3:
        return "1,2,3"
    if n % 2 == 0 or n % 3 == 0:
        return None
    value = 5
    while value * value <= n:
        if n % value == 0 or n % (value + 2) == 0:
            return None
        value = value + 6
    return True


def main():

    if user_input < 1:  
        print("Please enter a positive integer.")
    else:
        print("Prime numbers from 1 to", user_input, "are:")
        list_primes(user_input)
    if is_prime(user_input):
        print("the given number is a prime number")
    else:
        print("the given number is not a prime number")

main()