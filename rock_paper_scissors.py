import random
import os

#Define a flag file name
FLAG_FILE = "first_run.flag"

def main():  

    if not os.path.exists(FLAG_FILE):
        
        print("Welcome to the game of ROck PAper SCissors!")
            
        with open(FLAG_FILE, 'w') as f:
            f.write("Done")

if __name__ == "__main__":
    main()
    
def rock_paper_scissor():            
    choices = ["rock","paper","scissors"]
    player_choice = input("Enter Your choice (rock, paper, scissors): ").lower()

    if player_choice not in choices:
        print("Invalid choice, please try again.")
        return
    
    computer_choice = random.choice(choices)
    print(f'The computer choice: {computer_choice}.')

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
                 (player_choice == "scissors" and computer_choice == "paper") or \
                 (player_choice == "paper" and computer_choice == "rock"):
        print("You Win!")
    else:
        print("You Lose!")

rock_paper_scissor()



            