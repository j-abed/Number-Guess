#import the random module from the standard library
import random

#Set the number to guess
number_to_guess = random.randint(1, 100)

#track the number of guesses
guess_count = 0

#start the game

#The game will continue until the user guesses the correct number
while True:
    #Ask the user to guess a number
    guess = input("Guess a number between 1 and 100: ")
    #capture the user's guess
    guess = int(guess)  # Convert the string to an integer
    #increment the guess count by 1
    guess_count += 1
    
    #Check if the user's guess is correct
    if guess < number_to_guess: #If the guess is too low
        print("Too low!")
    elif guess > number_to_guess: #If the guess is too high
        print("Too high!")
    else: #the guess is correct
        print(f"Congratulations! You guessed the number in {guess_count} tries.")
        break #exit the loop, and in this case, the game
