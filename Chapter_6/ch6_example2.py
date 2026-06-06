import random  
mynumber = random.randint(0,100)  
guess = -1  
# print(mynumber) Are you trying to cheat?  
while guess != mynumber:  
    guess = int(input("guess my number: "))  
    if guess < mynumber: print("Go higher!")  
    elif guess > mynumber: print("Go lower!")  
    else: print("Great guess!")
