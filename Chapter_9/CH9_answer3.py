def return_laughing_string(input_string):  
    vowels = "aeiouAEIOU"  
    return "".join(["haha" if char in vowels else char for char in input_string])

print(return_laughing_string("apple")) # hahapplhaha
