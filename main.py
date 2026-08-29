import time
import sys
from storage import decode_to_json, encode_to_json
from passwords import *
from genarete import genarete_password


def main():
    choices = {
        "1" : "Add password",
        "2" : "Show passwords",
        "3" : "Search password",
        "4" : "Delete password",
        "5" : "Generate password",
        "6" : "Exit"
    }
    
    while True:
        title = "PASSWORD MANAGER"
        print("="*len(title)*3)
        print(" "*len(title)+title)
        print("="*len(title)*3+"\n")
        
        for key in choices.keys():
            print(f"{key}. {choices[key]}")
        
        choice = input("\nChoose an option: ")
        
        if choice in choices.keys():
            do_option(choice)
        else:
            print("\nWrong Input!")
            input("Press enter to continue")
        
         
            
            
def do_option(choice):
        data = decode_to_json()
        
        match choice:
            case "1":
                data.update(add_password())
                print(data)
                encode_to_json(data)
            case "2":
                print(data)
                show_passwords(data)
            case "3":
                search_password(data)
            case "4":
                encode_to_json(delete_password(data))
            case "5":
                password = genarete_password()
                print(f"\nGenerated Password: {password}")
            case "6":
                encode_to_json(data)
                sys.exit("Good bye!")
        
        input("Press Enter to continue")
            
        
    
if __name__ == "__main__":
    main()