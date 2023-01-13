import random
from ascii_art import rock, paper, scissors

def play_RPS():
    
    player_1 = 0
    guard = 0

    while True:
        player1 = input("Enter your pick (R/P/S): ").upper()
        bot = random.choice("RPS")
        print(f"You: {player1}")
        if player1 == "R":
            print(rock)
        elif player1 == "P":
            print(paper)
        elif player1 == "S":
            print(scissors)
        print(f"Guard: {bot}")
        if bot == "R":
            print(rock)
        elif bot == "P":
            print(paper)
        elif bot == "S":
            print(scissors)
        print("")

        if player1 == "R":
            if bot == "R":
                print("Nobody Wins")
            elif bot == "P":
                print("Guard Win, Paper Covers Rock!")
                guard += 1
                print(f"Scores are: You-{player_1}, Guard-{guard}")
            elif bot == "S":
                print("You Win, Rock Breaks Scissors!")
                player_1 += 1
                print(f"Scores are: You-{player_1}, Guard-{guard}")
        elif player1 == "P":
            if bot == "R":
                print("You Win, Paper Covers Rock!")
                player_1 += 1
                print(f"Scores are: You-{player_1}, Guard-{guard}")
            elif bot == "P":
                print("Nobody Wins.")
            elif bot == "S":
                print("Guard, Scissors cuts Paper!")
                guard += 1
                print(f"Scores are: You-{player_1}, Guard-{guard}")
        elif player1 == "S":
            if bot == "R":
                print("Guard Win, Rock beats Scissors!")
                guard += 1
                print(f"Scores are: You-{player_1}, Guard-{guard}")
            elif bot == "P":
                print("You Win, Scissors cuts Paper!")
                player_1 += 1
                print(f"Scores are: You-{player_1}, Guard-{guard}")
            elif bot == "S":
                print("Nobody Wins.")
        else:
            print("Invalid input, please enter only R/P/S.")
            print("")
            continue

        if player_1 == 3 or guard == 3:
            break

        print("")

    return player_1




