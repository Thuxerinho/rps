rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random

def again():
    play_again = input("Do you want to play again? Type 'y' for yes or 'n' for no.\n")
    if play_again == "y":
        rps()
    else:
        print("Thanks for playing!")
        exit()

def rps():
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    computer = [rock, paper, scissors]
    rps = ["rock", "paper", "scissors"]

    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number, you lose!")

    print(f"I choose {rps[user_choice]}{computer[user_choice]}.")

    computer_choice = random.randint(0, 2)
    print(f"Computer chose {rps[computer_choice]}{computer[computer_choice]}")

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    elif computer_choice > user_choice and computer_choice > 0:
        print("You lose!")
    elif user_choice > computer_choice and user_choice > 0:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw!")

    again()

rps()
