import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

emojis = {ROCK : '🪨', SCISSORS : ' ✂️', PAPER : '📃'}
choices = tuple(emojis.keys()) 
computer_score = 0
your_score = 0

def get_user_choice():
    while True:
        user_choice = input("rock, paper, scissors? (r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid Choices")


def declare_choices(user_choice,computer_choice):
        print(f"You choose {emojis[user_choice]}")
        print(f"Computer chose {emojis[computer_choice]}")


def determine_winner(user_choice,computer_choice):
    global your_score, computer_score
    if user_choice == computer_choice:
        print("Its a tie!")
        your_score += 1
        computer_score += 1

    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or 
        (user_choice == SCISSORS and computer_choice == PAPER) or 
        (user_choice == PAPER and computer_choice == ROCK)):
        print("You win")
        your_score += 1

    else:
        print("Computer Wins")
        computer_score += 1

def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)
        declare_choices(user_choice,computer_choice)
        determine_winner(user_choice,computer_choice)


        should_continue = input("do you want to continue? (y/n): ").lower()

        if should_continue == 'n':
            print("Thank you for playing")
            print(f'you scored {your_score} and computer scored {computer_score}')
            break
        
play_game()