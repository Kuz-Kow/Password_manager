import random
import string

def genarete_password(fields:dict) -> str:
    
    password = ""
    
    if not fields["password length"].strip().isdigit():
        print("Wrong length value!")
        fields ["password length"] = input("Password length: ")
        return genarete_password(fields)
        
        
        
    charecters = list(string.ascii_lowercase) + list(string.ascii_uppercase) + [f"{i}" for i in range(0,10)] + list(string.punctuation)
    
    
    for charecter in range(0, int(fields["password length"])):
        password = password + random.choice(charecters)
        
    
    return password

