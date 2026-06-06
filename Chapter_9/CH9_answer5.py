MORSE_CODE_DICT = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----'}

def convert_to_morse(text):  
    morse_output = []  
    for char in text.upper():  
        if char in MORSE_CODE_DICT:  
            morse_output.append(MORSE_CODE_DICT[char])  
        elif char == " ":  
            morse_output.append("/") # Use forward slash to indicate word spaces  
    return " ".join(morse_output)

print(convert_to_morse("Hello World"))
