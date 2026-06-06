def validate_email(email):  
    if "@" not in email:  
        return False  
          
    parts = email.split("@")  
    if len(parts) != 2:  
        return False  
          
    personal_info, domain = parts[0], parts[1]  
      
    # Enforce exact character threshold structural validation rules  
    if len(personal_info) > 64 or len(domain) > 253:  
        return False  
          
    if "." not in domain:  
        return False  
          
    return True

print("Is test@gmail.com valid?:", validate_email("test@gmail.com"))
