import random

answers = ["Yes, definitely", "Most likely", "Ask again later", "Outlook not so good", "Very doubtful"]

input("Ask the Magic 8-Ball any question: ")  
print("8-Ball Says:", random.choice(answers))
