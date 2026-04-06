                                 ###...Phone-Book...###
import re

contacts = {}

#Options, get user choice
def get_user_choice():
    print("\n|--------[MENU]-------|")
    print("|  1. Add Contact     |")
    print("|  2. View Contacts   |")
    print("|  3. Search Contact  |")
    print("|  4. Update Contact  |")
    print("|  5. Delete Contact  |")
    print("|  6. Exit            |")
    print("-----------------------")

    while True:
        choice = input("Enter your choice (1-6):").strip()
        if choice in ('1', '2', '3', '4', '5', '6'):
            return choice
            break
        else:
            print("⚠️  Invalid choice. Please enter a number between 1 and 6.\n")
            continue



#Validate name
def get_name():
    while True:
        name = input("Enter name: ").lower()
        if name == '':
            print("⚠️  Name cannot be empty.\n")
            continue
        return name
        break


#Validate Phone number
def get_phone_number():
    while True:
        phone_number = input("Enter phone number: ")
        if phone_number.isdigit() and len(phone_number) == 10:
            return phone_number
            break
        print("⚠️  Invalid phone number. Please enter 10 digits only.\n")
        continue


#Validate email
def get_email():
    while True:
        email = input(r"Enter email: ").strip()
        pattern = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        match = re.match(pattern, email)
        if match:
            return email
            break
        print("⚠️  Invalid email format. Please try again.\n")
        continue


#Validate address
def get_address():
    address = input("Enter address: ").strip()
    if address == '':
        print("⚠️  Adderess cannot be empty.\n")
    return address
   



#Add contacts into
def add_contact(name, phone_number, email, address):
    i = len(contacts)+1
    contacts[i] = {'name':name, 'phone_number': phone_number, 'email':email, 'address':address}
    print("Contact added successfully.")



#Show contact list
def show_contact_list(contacts):
    if len(contacts) > 0:
        for i in range(1, len(contacts)+1):
            print(f"{i}. {contacts[i]['name']}  |  {contacts[i]['phone_number']}")
    else:
        print("No contacts found.")


#Search contact via name/phone number
def search_contact(contacts):
    if len(contacts) > 0:
        search = input("Enter name or phone number: ").strip().lower()
        for i in range(1, len(contacts)+1):
            if search == contacts[i]['name'] or \
                search == contacts[i]['phone_number']:
                print(f"name         :  {contacts[i]['name']}")
                print(f"phone number :  {contacts[i]['phone_number']}")
                print(f"emil         :  {contacts[i]['email']}")
                print(f"address      :  {contacts[i]['address']}")
        else:
            print("No matching contacts found.")
    else:
        print("No contacts found. Please! Add contacts first.")



# def update_contact():



def main():
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("           Contact Book")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    while True:

        choice = get_user_choice()

        if choice == '1':
            print("\n_______________[Add New Contact]_______________")
            name = get_name()
            phone_number = get_phone_number()
            email = get_email()
            address = get_address()
            add_contact(name, phone_number, email, address)
            print("_____________________________________________\n")
            continue
        elif choice == '2':
            print("\n__________________[Contacts]___________________")
            show_contact_list(contacts)
            print("_____________________________________________\n")
            continue
        elif choice == '3':
            print("\n________________[Search Contact]_______________")
            search_contact(contacts)
            print("_______________________________________________\n")
            continue
        elif choice == '4':
            pass
        elif choice == '5':
            pass
        elif choice == '6':
            print("\n~ See you again!")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            break




if __name__ == '__main__':
    main()
