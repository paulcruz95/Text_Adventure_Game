from rps_ai import play_RPS
from ascii_art import theEnd, palace

# Functions
def gameOver(characterName, reasonOfLosing):
    print("")
    print(f"{characterName} died.")
    print(f"Reason: {reasonOfLosing}")

def rightAnswer1(characterName):
    print("")
    print("You passed.")
    print("")
    print(f"{characterName} brings the cure to the palace and healed the princess.")
    print(f"Because of {characterName}'s bravery, the princess fell inloved to him and they lived happily ever after.")
    print("")
    print(theEnd())
    print("")
    print("The End.")

def rewardMoney(characterName):
    print("")
    print(f"You chose the reward money as you answer")
    print(f"The guard is not satisfied with you answer and it killed you.")

    gameOver(characterName, "The guard killed you because of your greediness.")

def left(characterName):
    print("")
    print(f"There is a guard that looked like a big spider.")
    print(f"The guard said: 'I will let you pass if we played Rock, Paper, and Scissors.'")
    print("If you win 3 times, I'll let you passed.")

    play = input("Would you like to play? (Y/N): ").upper()
    if play == "Y":
        hero = play_RPS()
        
    elif play == "N":
        gameOver(characterName, "You had bitten by the big spider.")

    if hero == 3:
        print("")
        print("Guard: 'This is the first time that I lost to mortal...'")
        print(f"Guard asked you: 'What it is here you are looking for?'")
        
        while True:
            print("1. The cure for the sick princess")
            print("2. The reward money")

            userChoice = input(">>> ")

            if userChoice == "1":
                rightAnswer1(characterName)
                break
            elif userChoice == "2":
                rewardMoney(characterName)
                break
            else:
                print("Invalid input, please enter 1 or 2 only.")
                continue
    else:
        gameOver(characterName, "You had bitten by the big spider.")

def right(characterName):
    print("")
    print(f"You chose the right path, but the wrong one.")
    print(f"You continued travelling for days, but not seen anything except sand.")

    gameOver(characterName, "You died because of dehydration.")
    
def introduction(characterName):
    print(f"You are {characterName}, a mighty hero from the land of lunacia.")
    print("The king assigned you to find the cure for the princess.")
    print("The king said that he will grant you a big prize if you will find the cure.")
    print(f"The wizard warned you, '{characterName}, you will only succeed if you had the purest heart.'")
    print("")
    print("A few days later, after packing your things and readying for the journey.")
    print("You get away with your horse and on your way, you saw the two path.")
    print("Which way will you go: ")

    while True:
        print("1. Left")
        print("2. Right")

        userChoice = input(">>> ")
        if userChoice == "1":
            left(characterName)
            break
        elif userChoice == "2":
            right(characterName)
            break
        else:
            print("Invalid input, please enter 1 or 2 only.")
            continue

def newgame():
    while True:
        print(palace)
        print("Welcome to Text Adventure Game!")
        characterName = input("Enter your name: ")
        
        userChoice = input("Are you sure? (Y/N): ").upper()
        if userChoice == "Y":
            print("")
            introduction(characterName)
            break
        elif userChoice == "N":
            continue
        else:
            print("Invalid input, please enter only Y/N.")


if __name__ == "__main__":
    newgame()