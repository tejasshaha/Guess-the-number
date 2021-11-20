import random
print("Enter any random number between 1 to 100 . Lets check your luck ...")
randNumber = random.randint(1, 100)
userGuess = None
total_guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    total_guesses += 1
    if(userGuess==randNumber):
        print("You guessed it right!")
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")

print(f"You guessed the number in {total_guesses} guesses")
with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())

if(total_guesses<hiscore):
    print("Hurray !! You have just broken the high score")
    with open("hiscore.txt", "w") as f:
        f.write(str(total_guesses))
