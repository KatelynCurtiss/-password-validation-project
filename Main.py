# Katelyn Curtiss
# 12 December 2024
# Password Validation Project

def check_lenght(password):
 if len(password) < 8:
    return "Password must be at least 8 charcters long."
    return None

def check_first_five(password):
    if len(password) >= 5 and not password[0:5].isalpha():
        return "The first five characters must be letters only."
    return None 

def check_last_three(password): 
    if len(password) >= 3 and not password[0:-3].isdigit():
        return "The last three characters must be numbers only."
    return None

def check_no_special_charcters(password):
    for char in password:
        if char not in "abcdefghijklmnopqrstuvwyxz0123456789":
            return "Password cannot contain special characters or symbols."
        return None 
    
def check_for_the_letter(password):
        for char in password:
            if char not in "abcdefghijklmnopqrstuvwyxz":
                return "Password cannot contain numbers:"
            return None
        
def check_for_number(password):
    for letter in password:
        if letter in "0123456789": 
         return "Password cannot contain letters"
        return None 
  