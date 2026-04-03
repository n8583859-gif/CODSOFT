                                    # Calculator with simple functionality

#
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("                  Simple Calculator                       ")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

while True:
    #Validate proceed or quit choice
    choice = input("Press `ENTER` to start a calculation\nType 'q' to quit\nYour choice: ").lower()
    if (choice == 'q'):
        print("Thanks for using the calculator. See you next time!")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        proceed = False
        break
    elif (choice == ""):
        proceed = True
        break
    else:
        continue



#Number and operator inputs
while proceed:

    #Validate first number input from user
    while True:
        try:
            num1 = float(input("Enter the first number: "))
        except ValueError as ve:
            print("⚠️  Please! try again with a valid number.")
            continue
        else:
            break

    #Validate operator input from user
    while True:
        operator = input("Choose an operation (+, -, *, /):").strip()
        if operator not in ('+', '-', '*', '/'):
            print("⚠️  Invalid operation. Please choose from +, -, *, /")
            continue
        else:
            break


    #Validate second number input from user
    while True:
        try:
            num2 = float(input("Enter the second number: "))
        except ValueError as ve:
            print("⚠️  Please! try again with a valid number.")
            continue
        else:
            break
    

