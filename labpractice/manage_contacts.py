# Omyaasree Balaji
# Manage contacts using dictionary

def main():

	phonebook = {}

	while True:

		print ("1. add a contact to your phonebook")
		print ("2. change the phone number ")
		print ("3. delete phone number of a person ")
		print ("4. Display the contacts list")
		print ("5. Exit (this will save your contacts)")

		user_input=int(input("enter your choice :"))

		if user_input == 1:
			add_entry(phonebook)

		elif user_input == 2:
			change_entry(phonebook)

		elif user_input == 3:
			delete_contact(phonebook)

		elif user_input == 4:
			display_contacts(phonebook)

		elif user_input == 5:
			print("Exiting the program.")
			contact_list(phonebook)
			break

		else:
			print("Invalid choice. Please select a valid option (1/2/3/4/5).")



def add_entry(phonebook):
	user_name = str(input("enter the name of the contact: "))
	user_contact = int(input("enter the phone number of the person: "))
	phonebook[user_name] = user_contact
	print(f"added name: {user_name} to contacts with phone number: {user_contact}")



def change_entry(phonebook):
	user_name = str(input("enter the name of the contact: "))
	if user_name in phonebook:
		user_contact = int(input(f"enter the new contact number for {user_name}: "))
		phonebook[user_name] = user_contact
		print(f"changed phone number of {user_name} to phone number: {user_contact}")

	else:
		print(f"{user_name} not found in contacts")


def delete_contact(phonebook):
    user_name = input("Enter the name you want to delete: ")
    if user_name in phonebook:
        del phonebook[user_name]
        print(f"Deleted {user_name} from contacts.")
    else:
        print(f"{user_name} not found in contacts.")


def display_contacts(phonebook):
    print("Contacts List:")
    for name, phone in phonebook.items():
        print(f"{name} \t\t {phone}")


def contact_list(phonebook):
    file = open("contacts.txt" , "w")
    for items in phonebook:
        file.write(f"{items} \t {phonebook[items]}\n")
    print("Inventory has been saved to contacts.txt")



main()