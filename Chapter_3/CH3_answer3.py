import random

secret_number = random.randint(1, 100)  
guess = -1

print("I have picked a number between 1 and 100\. Guess it!")

while guess != secret_number:  
    guess = int(input("Enter your guess: "))  
    if guess < secret_number:  
        print("Go higher!")  
    elif guess > secret_number:  
        print("Go lower!")  
    else:  
        print("Great guess! You got it!")
