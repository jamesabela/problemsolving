import random

num1 = random.randint(1, 12)  
num2 = random.randint(1, 12)  
operator = random.choice(["+", "-", "*"])

question_str = f"{num1} {operator} {num2}"  
# Use eval to solve the equation string safely behind the scenes  
correct_answer = eval(question_str)

user_ans = int(input(f"What is {question_str}? "))

if user_ans == correct_answer:  
    print("Brilliant work! That's correct.")  
else:  
    print(f"Not quite. The correct answer was {correct_answer}.")
