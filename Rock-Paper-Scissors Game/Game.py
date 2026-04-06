                            ###...Rock-Paper-Scissors (Game)...###

import random as rnd

options = {'1':'Rock', '2':'Paper', '3':'Scissors'}

#User choice
def get_user_choice():
    while True:
        print("\n1.Rock  |  2.Paper  |  3.Scissors")
        choice = input("Enter your choice (1/2/3):").strip()
        if choice in options:
            return choice
        print("⚠️  Invalid choice. Please enter 1/2/3\n")



#Computer choice
def get_computer_choice():
        return rnd.choice(list(options.keys()))



#Determine winner
def determine_winner(user, computer):
    if user == computer:
        return 'tie'
    elif user == '1' and computer == '3' or \
         user == '2' and computer == '1' or \
         user == '3' and computer == '2':
        return 'user'
    else:
        return 'computer'



#Display result
def display_result(user, computer, outcome):
    print("\n\n------------- RESULT -------------")
    print(f"You Choose      -> {options[user]}")
    print(f"Computer Choose -> {options[computer]}")

    if outcome == "user":
        print("Result         -> You Win🎉")
    elif outcome == "computer":
        print("Result         -> You Lose")
    else:
        print("Result         -> Tie")

    print("----------------------------------\n")



#Play again
def play_again():
    while True:
        again = input("Press `ENTER` to play again or Type 'q' to quite: ").lower().strip()
        if (again == 'q'):
            return False
        elif (again == ''):
            return True
        else:
            continue



# Display final score
def display_final_result(score):
            print("\n===============[FINAL_RESULT]===============")
            print(f"You Won      -> {score['user']} Times")
            print(f"Computer Won -> {score['computer']} Times")
            print(f"Tie Game     -> {score['tie']} Times")
            print("============================================")
            print("Thanks for play this game. See you again!")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")



#user interface
def main():
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("          Rock-Paper-Scissors 🎮")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

    score = {'user':0, 'computer':0, 'tie':0}

    while True:
        user = get_user_choice()
        computer = get_computer_choice()
        outcome = determine_winner(user, computer)

        #Update score
        score[outcome] += 1

        #Print result
        display_result(user, computer, outcome)

        #Print final result
        if not play_again():
             display_final_result(score)
             break



if __name__ == "__main__":
    main()
