# omyaasree
# cs110
# project 3 part 2

import csv
from dog import Dog
from cat import Cat
from fish import Fish
from bird import Bird

file_path = 'pets.csv'
def read_pets_csv(file_path):
    pets = []

    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            pet_type = row[0]
            name = row[1]
            birthdate = row[2]

            if pet_type == 'Dog':
                breed = row[3]
                color = row[4]
                pets.append(Dog(name, birthdate, breed, color))
            
            elif pet_type == 'Cat':
                breed = row[3]
                color = row[4]
                pets.append(Cat(name, birthdate, breed, color))
            
            elif pet_type == 'Fish':
                fish_type = row[3]
                color = row[4]
                pets.append(Fish(name, birthdate, fish_type, color))
            
            elif pet_type == 'Bird':
                bird_type = row[3]
                color = row[4]
                pets.append(Bird(name, birthdate, bird_type, color))
    return pets

def print_pet_names(pets):
    for pet in pets:
        print(pet.get_name())


def pet_type(pets, user_type):
    for pet in pets:
        if user_type.lower() == type(pet).__name__.lower():
            print(pet.get_name())
            print(pet.display_info())

def binary_search(pets, search_name):
    n = len(pets)  # Get the length of the array
      
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return
 
    for i in range(1, n):  # Iterate over the array starting from the second element
        key = pets[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key.get_name().strip() < pets[j].get_name().strip():  # Move elements greater than key one position ahead
            pets[j+1] = pets[j]  # Shift elements to the right
            j -= 1
        pets[j+1] = key
    low = 0
    high = len(pets) - 1

    while low <= high:
        current_index = (low + high) // 2
        current_name = pets[current_index].get_name()

        if current_name == search_name:
            return current_index 
        elif current_name < search_name:
            low = current_index + 1
        else:
            high = current_index - 1

    return -1

def insertionSort(pets):
    n = len(pets)  # Get the length of the array
      
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return
 
    for i in range(1, n):  # Iterate over the array starting from the second element
        key = pets[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key.get_name().strip() < pets[j].get_name().strip():  # Move elements greater than key one position ahead
            pets[j+1] = pets[j]  # Shift elements to the right
            j -= 1
        pets[j+1] = key

    for item in pets:
        print(item, end=" ")

    print()



# def insertion_sort_pets_by_name(pets):

#     for item in pets:
#         print(item, end=" ")

#     print()

#     for i in range(1, len(pets)):
#         # current_pet = pets[i]
#         j = i - 1

#         while j >= 0 and pets[j+1].get_name() < pets[j].get_name():
#             temp = pets[j+1]

#             pets[j + 1] = pets[j]
#             pets[j] = temp



#             j -= 1



#     for pet in pets:
#         print(pet.get_name())


# def insertion_sort_pets_by_name(pets):
#     for i in range(1, len(pets)):
#         current_pet = pets[i]
#         j = i - 1

#         while j >= 0 and current_pet.get_name() < pets[j].get_name():
#             pets[j + 1] = pets[j]
#             j -= 1

#         pets[j + 1] = current_pet
#         print(current_pet.get_name())


def main():
    pets = read_pets_csv('pets.csv')

    total_pets = len(list(csv.reader(open('pets.csv'))))

    while True:

        print("1. To print the whole information")
        print("2. To print all the pet names of the given files")
        print("3. to print pets of a certain type")
        print("4. to search for a pet")
        print("5. to print all the pets in the sorted order")
        print("6. exit")

        user_input = int(input("Enter your choice: "))

        if user_input == 1:
            for pet in pets:
                print(pet.display_info())

        elif user_input == 2:
            print_pet_names(pets)

        elif user_input == 3:
            user_type = str(input("enter your pet type"))
            pet_type(pets, user_type)

        elif user_input == 4:
            search_name = input(" please note that the input is case sensitive hence input the name with first letter as a capital letter \nEnter the name of the pet to search: ")
            index = binary_search(pets, search_name)
            if index == -1:
                print(f"Pet '{search_name}' not found in the list.")
            else:
                print(f"Pet found at index {index}")
                print(pets[index].display_info())

        elif user_input == 5:
            print("Sorted list of pets by name:")
            insertionSort(pets)

        elif user_input == 6:
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

        # Check if the length of the list is equal to the expected number of pets
        if len(pets) == total_pets:
            print("\nSuccessfully created pet objects for all pets in the CSV file.\n")
        else:
            print("Error: Number of pets in the list does not match the number of pets in the CSV file.\n")

if __name__ == "__main__":
    main()
