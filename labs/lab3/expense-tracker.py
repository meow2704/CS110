print("WELCOME TO EXPENSE TRACKER")

transportation = 0
food = 0
medical = 0
entertainment = 0

transportation_count = 0
food_count = 0
medical_count = 0
entertainment_count = 0


def get_expense():
    global transportation, food, medical, entertainment, transportation_count, food_count, medical_count, entertainment_count
    while True:
        expense = int(input("Enter your expense: "))
        
        category = int(input("Enter a category (1-transportation, 2-food, 3-medical, 4-entertainment): "))

        if category == 1:
            transportation += expense
            transportation_count +=1
        elif category == 2:
            food += expense
            food_count += 1
        elif category == 3:
            medical += expense
            medical_count +=1
        elif category == 4:
            entertainment += expense
            entertainment_count += 1
        else:
            print("Enter a valid input between 1, 2, 3, 4")

        another_expense = input("Do you want to enter another expense? (y/n): ")
        if another_expense.lower() != "y":
            break


def display_expense():
    print("Expense Report: \n")


    if transportation_count > 0:
        print(f"total Transportation expense: {transportation}")
        print(f"Transportation Average: ${transportation / transportation_count:.2f} \n")
    else: 
        print("there is not transportation expense")
        print("the average transportation expense is 0\n")

    if food_count > 0:
        print(f"total Food expense: {food}")
        print(f"Food Average: ${food / food_count:.2f} \n")
    else: 
        print("there is not food expense")
        print("the average food expense is 0\n")


    if medical_count > 0:
        print(f"total Medical expense: {medical}")
        print(f"Medical Average: ${medical / medical_count:.2f} \n")
    else: 
        print("there is not medical expense")
        print("the average medical expense is 0\n")

    if entertainment_count > 0:
        print(f"total entertainment expense: {entertainment}")
        print(f"Entertainment Average: ${entertainment / entertainment_count:.2f} ")
    else: 
        print("there is not entertainment expense")
        print("the average entertainment expense is 0\n")

def main():
    get_expense()
    display_expense()

main()