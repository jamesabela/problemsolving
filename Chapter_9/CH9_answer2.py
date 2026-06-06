def get_validated_integer(prompt):  
    while True:  
        user_input = input(prompt).strip()  
        # Validate using string checking methods before casting to integer format type  
        if user_input.lstrip('-').isnumeric():  
            return int(user_input)  
        else:  
            print("Invalid structure entry. Please input a whole number!")

age = get_validated_integer("Enter your age: ")  
print(f"Stored input verified: {age}")
