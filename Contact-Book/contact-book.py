                                 ###...Phone-Book...###
import re

contacts = {}

#Options, get user choice
def get_user_choice():
    print("\n┌━━━━━━━[MENU]━━━━━━━━┐")
    print("|  1. Add Contact     |")
    print("|  2. View Contacts   |")
    print("|  3. Search Contact  |")
    print("|  4. Update Contact  |")
    print("|  5. Delete Contact  |")
    print("|  6. Exit            |")
    print("└━━━━━━━━━━━━━━━━━━━━━┘")

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
            contact_name = contacts[i]['name']
            contact_phone_number = contacts[i]['phone_number']
            contact_email = contacts[i]['email']
            contact_address = contacts[i]['address']
            print(f"{i}. {contact_name} | {contact_phone_number} | {contact_email} | {contact_address}")
    else:
        print("No contacts found.")



#Search contact via name/phone number
def search_contact(contacts):
    search = input("Enter name or phone number: ").strip().lower()
    for i in range(1, len(contacts)+1):
        if search == contacts[i]['name'] or \
            search == contacts[i]['phone_number']:
            print(f"name         :  {contacts[i]['name']}")
            print(f"phone number :  {contacts[i]['phone_number']}")
            print(f"email        :  {contacts[i]['email']}")
            print(f"address      :  {contacts[i]['address']}")
    else:
        print("No matching contacts found.")



#Update Contact
def update_contact(contacts):
    update_details = input("Enter name or phone number to update: ").lower().strip()
    for i in range(1, len(contacts)+1):
        if update_details == contacts[i]['name'] or \
            update_details == contacts[i]['phone_number']:
            print("\nLeave field empty to keep current value.")
            update_name = input("Enter new name: ").lower().strip()
            update_phone_number = input("Enter new phone number: ").lower().strip()
            update_email = input("Enter new email: ").lower().strip()
            update_address = input("Enter new address: ").lower().strip()
            if update_name:
                contacts[i]['name'] = update_name
            if update_phone_number:
                contacts[i]['phone_number'] = update_phone_number
            if update_email:
                contacts[i]['email'] = update_email
            if update_address:
                contacts[i]['address'] = update_address
            print("Contact updated successfully.")
        break
    else:
        print("No matching contacts found.")




#Delete contact
def delete_contact(contacts):
    delete_number = input("Enter name or phone number to delete: ").strip().lower()
    for i in range(1, len(contacts)+1):
        if delete_number == contacts[i]['name'] or \
            delete_number == contacts[i]['phone_number']:
            while True:
                think_again = input("⚠️⚠️  Are you sure you want to delete this contact? (y/n): ").lower().strip()
                if think_again == 'y':
                    contacts.pop(i)
                    print("Contact deleted successfully.")
                    break
                elif think_again == 'n':
                    break
                else:
                    continue
            break
    else:
        print("No matching contacts found.")






#User interface
def main():
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("           Contact Book")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    while True:

        choice = get_user_choice()

        #Add new contact
        if choice == '1':
            print("\n_______________[Add New Contact]_______________")
            name = get_name()
            phone_number = get_phone_number()
            email = get_email()
            address = get_address()
            add_contact(name, phone_number, email, address)
            print("_____________________________________________\n")
            continue

        #View all contacts
        elif choice == '2':
            print("\n__________________[Contacts]___________________")
            show_contact_list(contacts)
            print("_____________________________________________\n")
            continue

        #Search contact
        elif choice == '3':
            print("\n________________[Search Contact]_______________")
            search_contact(contacts)
            print("_______________________________________________\n")
            continue

        #Update contct
        elif choice == '4':
            print("\n________________[Update Contact]_______________")
            update_contact(contacts)
            print("_______________________________________________\n")

        #Delete contact
        elif choice == '5':
            print("\n________________[Delete Contact]_______________")
            delete_contact(contacts)
            print("_______________________________________________\n")

        #Exit
        elif choice == '6':
            print("\n~ See you again!")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            break




if __name__ == '__main__':
    main()
