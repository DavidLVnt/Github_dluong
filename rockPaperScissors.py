import random
while True:
    player = input("Enter your weapon(rock, paper, scissors): ")
    print("Your weapon:", player)
    possibleActions= ["rock", "paper", "scissors"]
    computerPlayer = random.choice(possibleActions)
    print("Computer weapon:", computerPlayer)
    if player == computerPlayer:
        print("Both players selected", player, "It's tie game!")
    elif player == "rock":
        if computerPlayer == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper cover rock! You lose.")
    elif player == "paper":
        if computerPlayer == "rock":
            print("Paper cover rock! You win!")
        else:
            print("Scissors cut paper! You lose.")
    elif player == "scissors":
        if computerPlayer == "paper":
            print("Scissors cut paper! You win")
        else:
            print("Rock smashes Scissors! You lose.")

    playMore = str(input("Do you want play again? (Yes/No): "))
    if playMore != "Yes":
        break