hour = int(input("Enter the hour (1-12): "))  
period = input("Enter am or pm: ").strip().lower()

if period == "am":  
    if hour == 12:  
        print("24-Hour Format: 0")  
    else:  
        print(f"24-Hour Format: {hour}")  
elif period == "pm":  
    if hour == 12:  
        print("24-Hour Format: 12")  
    else:  
        print(f"24-Hour Format: {hour + 12}")  
else:  
    print("Invalid period entered.")
