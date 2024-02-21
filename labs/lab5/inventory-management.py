#Omyaasree Balaji
#CS110
#lab5 - lists and files


import csv
#importing csv library to code


def main():
    names , prices, quantities = read_inventory()
    # assigning separate lists

    while True:
        print("Menu:")
        print("1. Display inventory")
        print("2. Add a new item")
        print("3. Delete item")
        print("4. Update the price or quantity item")
        print("5. Total valuee of the inventory")
        print("6. Write Inventory to File")
        print("7. Quit")

        user_input = input("Enter your choice: ")

        if user_input == "1":
            display_inventory(names, prices, quantities)
        elif user_input == "2":
            add_item(names, prices, quantities)
        elif user_input == "3":
            delete_item(names, prices, quantities)
        elif user_input == "4":
            update_item(names, prices, quantities)
        elif user_input == "5":
            total_inventory_value(names, prices, quantities)
        elif user_input == "6":
            write_inventory(names, prices, quantities)
        elif user_input == "7":#choice if the user wants to quit the program
            break
        else:
            print("Invalid choice. Please choose a valid option.")


# funtion for opening and reading the content of the inventory
def read_inventory():

    names = []
    prices = []
    quantities = []
    file = open("inventory.csv", "r")
    reader = csv.reader(file)

    for row in reader:
        names.append(row[0])
        prices.append(row[1])
        quantities.append(row[2])

    return names, prices, quantities


# function to display inventory 
def display_inventory(names, prices, quantities): #assigning different variables
    print("Inventory:")
    for i in range (len(names)): # for iterating through all the lists in the inventory 
        print(f"{names[i]}, Price: ${prices[i]}, Quantity: {quantities[i]}")


# function to add new items to the inventory
def add_item(names, prices, quantities):
    name = input("Enter the name of the new item: ")
    price = float(input("Enter the price of the new item: "))
    quantity = int(input("Enter the quantity of the new item: "))
    names.append(name)
    prices.append(int(price))
    quantities.append(float(quantity))
    print("Item added to the inventory.")
    display_inventory(names, prices, quantities)


#function to delete item from the inventory
def delete_item(names, prices, quantities):
    item_delete = input("Enter the name of the item to delete: ")
    try:
        index = names.index(item_delete)
        del names[index]
        del prices[index]
        del quantities[index]
        print(f"{item_delete} has been deleted from the inventory.")
    except ValueError:
        print(f"{item_delete} not found in the inventory.")


#funtion to update the information of an iten in the inventory
def update_item(names, prices, quantities):
    item_update = input("Enter the name of the item to update: ")
    if item_update in (names):        
        index = names.index(item_update)
        print("1. Update price")
        print("2. Update quantity")
        #different choices to update price or quantity of the item
        choice = int(input("Enter your choice: "))
        if choice == 1:
            new_price = float(input("Enter the new price: "))
            prices[index] = new_price
            print("Price updated.")
        elif choice == 2:
            new_quantity = int(input("Enter the new quantity: "))
            quantities[index] = new_quantity
            print("Quantity has been updated.")
        else:
            print("Invalid choice.")
    else:
        print(f"{item_update} not found in the inventory.")



# function to find the total value of the inventory
def total_inventory_value(names, prices, quantities):
    total_value = 0
    for i in range(1 , len(names)):# from range 1 not 0 as the value start from 2nd line of the inventory
        total_value += float(prices[i]) * int(quantities[i])
    print(f"Total inventory value: ${total_value:.2f}")#value of the inventory uptop 2 decimal places
    


#function to write the updated inventory to a new output file 
def write_inventory(names, prices, quantities):
    file = open("inventory_output.csv" , "w")
    for i in range (len(names)):
        file.write(f"{names[i]}, {prices[i]}, {quantities[i]}\n")
    print("Inventory has been saved to inventory_output.csv")


main()