import random
import string

def genarete_password():
    
    password = ""
    
    try:
        length = int(input("Password length: "))
    except ValueError:
        print("Wrong input!")
        return genarete_password()
        
    charecters = list(string.ascii_lowercase) + list(string.ascii_uppercase) + [f"{i}" for i in range(0,10)] + list(string.punctuation)
    
    
    for charecter in range(0, length):
        password = password + random.choice(charecters)
        
    
    return password

