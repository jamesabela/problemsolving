import random

students = ["James", "John", "Mark", "Rick", "Sarah", "Emily", "Chloe", "Alex"]

# Shuffle the underlying index sequence explicitly  
random.shuffle(students)

print("Classroom Study Partners Assigned:")  
for i in range(0, len(students), 2):  
    # Ensure matching pairs print out cleanly  
    if i + 1 < len(students):  
        print(f"{students[i]} <---> {students[i+1]}")  
    else:  
        print(f"{students[i]} is working solo/in a group of three.")
