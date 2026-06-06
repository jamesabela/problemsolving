role = input("Are you a teacher or a student? (teacher/student): ").strip().lower()

if role == "teacher":  
    print("You are truly awesome!")  
elif role == "student":  
    print("You are incredibly awesome too!")  
else:  
    print("Everyone is awesome in their own way!")
