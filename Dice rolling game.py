import random

while True:

    choice=input("Do u wanna play the game? (Y/N) :").lower()
    if choice=="y":
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        print(f"The dice rolled 🎲 🎲: {dice1} and {dice2}")

    elif(choice=="n"):
        print("Thanks for playing!...👋👋👋")
        break
    else:
        print("Invalid choice")