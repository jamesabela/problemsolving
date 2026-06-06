import random

comments = [  
    "is an enthusiastic learner who seems to enjoy school.",  
    "exhibits a positive outlook and attitude in the classroom.",  
    "shows initiative and looks for new ways to get involved.",  
    "strives to reach their full potential."  
]

num_students = int(input("How many student reports do you need to write? "))

for i in range(num_students):  
    student_name = input(f"Enter name for student {i + 1}: ")  
    chosen_comment = random.choice(comments)  
    print(f"Report Output -> {student_name} {chosen_comment}
")
