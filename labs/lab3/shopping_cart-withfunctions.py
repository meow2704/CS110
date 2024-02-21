#defining a function that display the menu (asks for quatity of each item and shows the total cost)
def display_menu():
    print("WELCOME TO HEALTHY FRUITS SHOP")

    rasp = 0
    straw = 0
    apple = 0
    mango = 0

    rasp_input = input("Enter the number of pounds of raspberries you would like to have ($1.75 per pound): ")
    while rasp_input.isdigit() == False:
        rasp_input = input("Please enter valid numeric quantities: ")
    rasp = int(rasp_input)


    straw_input = input("Enter the number of pounds of strawberries you would like to have ($1.25 per pound): ")
    while straw_input.isdigit() == False:
        straw_input=input("please enter valid quantities: ")
    straw = int(straw_input)

    apple_input = input("Enter the number of apples you would like to have ($0.5 per apple): ")
    while apple_input.isdigit() == False:
        apple_input=input("please enter valid quantities: ")
    apple = int(apple_input)

    mango_input = input("Enter the number of mangoes you would like to have ($1.75 per mango): ")
    while mango_input.isdigit() == False:
        mango_input=input("please enter valid quantities: ")
    mango = int(mango_input)

    cost = (rasp * 1.75) + (straw * 1.25) + (apple * 0.5) + (mango * 1.75)
    print("The total cost of your purchase is $", cost)
    return cost

#defines a function that recieves the amount from the customer and also validates it
def get_payment(cost):
    while True:
        cost1 = float(input("Enter the amount you would like to pay: "))
        if cost1 >= cost:
            due = cost1 - cost
            print(f"The amount due by the shop is ${due:.2f}")
            return due
        else:
            print("Insufficient funds. Please enter a valid amount.")

#defining a function that ouputs the amount due from the shop to the customer
def calculate_change(due):
    num5 = int(due // 5)
    due = due - num5 * 5

    num1 = int(due // 1)
    due = due - num1 * 1

    quarters = int(due // 0.25)
    due = due - quarters * 0.25

    dimes = int(due // 0.1)
    due = due - dimes * 0.1

    nickels = int(due // 0.05)
    due = due - nickels * 0.05

    pennies = int(due * 100)

    print(f"Give the customer {num5}$5 notes, {num1}$1 notes, {quarters} quarters, {dimes} dimes, {nickels} nickels, {pennies} pennies")
    return


#defining the main funtion which calls all sub functions
def main():
    cost2 = display_menu()
    due1 = get_payment(cost2)
    calculate_change(due1)

main()