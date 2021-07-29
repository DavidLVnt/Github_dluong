import random
count = 0
while True:
    randomNum = random.randint(1, 9)
    print(randomNum)
    userGuess = int(input("Enter your number: "))
    print(userGuess)
    if userGuess == randomNum:
        print("The number guessed and random number is the same")
    elif userGuess > randomNum:
        print(userGuess, "greater than", randomNum, "your guess too high")
    else:
        print("Your guess too low")
    stopGame = str(input("Do you want exit game? (Yes/No): "))
    count += 1
    print("Total guess time:", count)
    if stopGame == "Yes":
        break