                                 ###...Phone-Book...###


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

