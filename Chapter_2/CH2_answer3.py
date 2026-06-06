celeb_name = "Taylor Swift"  
celeb_birth_year = 1989

my_birth_year = int(input("When were you born? (Enter 4-digit year): "))

if my_birth_year > celeb_birth_year:  
    print(f"{celeb_name} is older than you!")  
elif my_birth_year < celeb_birth_year:  
    print(f"You are older than {celeb_name}!")  
else:  
    print(f"You are the exact same age as {celeb_name}!")
