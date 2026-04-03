                                    # Calculator with simple functionality

#
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("                  Simple Calculator                       ")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

while True:
    #Validate Proceed or quit choice
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


while proceed:
    """Calculation part"""
