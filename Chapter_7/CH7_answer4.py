def make_it_laugh(input_string):  
    vowels = "aeiouAEIOU"  
    modified_string = ""  
    for char in input_string:  
        if char in vowels:  
            modified_string += "haha"  
        else:  
            modified_string += char  
    print(modified_string)

make_it_laugh("Hello World") # Hhahalllaho Whaharld -> Hhahalllaho Whaharld
