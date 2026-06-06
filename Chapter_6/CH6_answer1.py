import random

answer = input("What is the capital of Australia? ").strip().lower()

if answer == "canberra":  
    bonus_points = random.randint(10, 50)  
    print(f"Correct! You have been randomly awarded {bonus_points} bonus points!")  
else:  
    print("Incorrect answer.")
