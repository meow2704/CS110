n=int(input("enter a positive number"))

fib1=1
fib2=1

if n==1 or n==2:
	print(f"the {n}th number of the fibonacci series is :1")
else:
	for i in range(3,n+1):
		fib_new=fib1+fib2
		fib1=fib2
		fib2=fib_new
	print(f"the {i}th number in the fibonacci series is {fib_new}")



# n = int(input("Enter a positive number: "))

# fib1 = 0
# fib2 = 1

# if n == 1:
# 	print(f"the 1st number of the series is {fib1}")

# if n == 2:
#     print(f"The {n}th number of the Fibonacci series is: {fib2}")
# else:
#     for i in range(3, n + 1):
#         fib_new = fib1 + fib2
#         fib1 = fib2
#         fib2 = fib_new
#     print(f"The {i}th number in the Fibonacci series is: {fib_new}")


    
n = int(input("Enter a positive number: "))

fib1 = 0
fib2 = 1

if n == 1:
    print(f"The 1st number of the series is {fib1}")
elif n == 2:
    print(f"The 2nd number of the series is {fib2}")
else:
    for i in range(3, n + 1):
        fib_new = fib1 + fib2
        fib1 = fib2
        fib2 = fib_new
    print(f"The {n}th number in the Fibonacci series is: {fib_new}")
