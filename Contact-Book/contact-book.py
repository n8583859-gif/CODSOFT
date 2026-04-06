                                 ###...Phone-Book...###
import re

contact = {}

def get_user_choice():
    print("|--------[MENU]-------|   ")
    print("|  1. Add Contact     |")
    print("|  2. View Contacts   |")
    print("|  3. Search Contact  |")
    print("|  4. Update Contact  |")
    print("|  5. Delete Contact  |")
    print("|  6. Exit            |")
    print("-----------------------")

    while True:
        choice = input("Enter your choice (1-6):").strip()
        try:
            choice = int(choice)
            if choice not in range(1,7):
                raise ValueError
        except ValueError:
            print("⚠️  Invalid choice. Please enter a number between 1 and 6.")
            continue
        break



def get_name():
    print("--- Add New Contact ---")

    while True:
        name = input("Enter name: ").lower()
        if name == '':
            print("⚠️  Name cannot be empty.")
            continue
        return name
        break



def get_phone_number():
    while True:
        phone_number = input("Enter phone number: ")
        if phone_number.isdigit() and len(phone_number) == 10:
            return phone_number
            break
        print("⚠️  Invalid phone number. Please enter 10 digits only.")
        continue



def get_email():
    while True:
        email = input(r"Enter email: ").strip()

        pattern = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        match = re.match(pattern, email)

        if match:
            return email
            break
        print("⚠️  Invalid email format. Please try again.")
        continue



def get_address():
    address = input("Enter address: ").strip()
    if address == '':
        print("⚠️  Adderess cannot be empty.")
    return address
   


def add_contact(name, phone_number, email, address):
    i = len(contact)+1
    contact.update({i : {'name':name, 'phone_number': phone_number, 'email':email, 'address':address}})
    print("Contact added successfully.")



def show_contact_list(contact):
    if len(contact) > 0:
        for i in range(1, len(contact)+1):
            print(f"{i}. {contact[i]['name']}  |   {contact[i]['phone_number']}")
    else:
        print("No contacts found.")

