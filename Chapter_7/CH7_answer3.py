import os  
import platform

def clear_screen():  
    # Detect underlying execution runtime properties to call correct shell codes  
    if platform.system().lower() == "windows":  
        os.system("cls")  
    else:  
        os.system("clear")

# Testing the routine  
clear_screen()
