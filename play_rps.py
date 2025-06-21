import random

print("Winning rules of the game ROCK PAPER SCISSORS are:")
print(" ")
print("Rock vs Paper -> Paper wins \nRock vs Scissors -> Rock wins \nPaper vs Scissors -> Scissors wins")
print(" ")
print("Enter your choice \n1 - Rock \n2 - Paper \n3 - Scissors")

rock = 1
paper = 2
scissors = 3

your_choice = int(input("Enter your choice: "))

if your_choice == rock:
    print("User choice is: Rock")
elif your_choice == paper:
    print("User choice is: Paper")
elif your_choice == scissors:
    print("User choice is: Scissors")
else:
    print("Invalid Entry")


print("Now it's Computer's Turn...")
computer_choice = random.randint(1,3)

if computer_choice == rock:
    print("Computer choice is: Rock")
elif computer_choice == paper:
    print("Computer choice is: Paper")
elif computer_choice == scissors:
    print("Computer choice is: Scissors")
else:
    print("Invalid Entry")

print("")