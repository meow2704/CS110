n = 5

# Print upper part of the diamond
for i in range(n):
    for j in range(i, n-1):
        print(' ', end=" ")
    for j in range(i+1):
        print("*", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()

# Print lower part of the diamond
for i in range(n-2, -1, -1):
    for j in range(n-1, i, -1):
        print(' ', end=" ")
    for j in range(i+1):
        print("*", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()
