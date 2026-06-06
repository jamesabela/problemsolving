team_a = input("Enter Team 1 Name: ")  
team_b = input("Enter Team 2 Name: ")

print(f"
Enter scoring stats for {team_a}:")  
tries_a = int(input("Tries: "))  
conv_a = int(input("Conversions: "))  
pen_a = int(input("Penalties: "))

print(f"
Enter scoring stats for {team_b}:")  
tries_b = int(input("Tries: "))  
conv_b = int(input("Conversions: "))  
pen_b = int(input("Penalties: "))

# Score calculations (Rugby Union: Try = 5, Conversion = 2, Penalty = 3)  
score_a = (tries_a * 5) + (conv_a * 2) + (pen_a * 3)  
score_b = (tries_b * 5) + (conv_b * 2) + (pen_b * 3)

print(f"
Final Score Matrix:")  
print(f"{team_a}: {score_a} points ({tries_a} Tries, {conv_a} Convs, {pen_a} Pens)")  
print(f"{team_b}: {score_b} points ({tries_b} Tries, {conv_b} Convs, {pen_b} Pens)")
