import time
import sys
from storage import decode_to_json, encode_to_json
from passwords import *
from genarete import genarete_password


choices : dict [str , str]= {
        "1" : "Add password",
        "2" : "Show passwords",
        "3" : "Search password",
        "4" : "Delete password",
        "5" : "Generate password",
        "6" : "Exit"
    }

fields : dict[str , list[str]] = {
    "Add password": ["website", "username", "password"],
    "Search password" : ["website"],
    "Delete password" : ["website"],
    "Generate password" : ["password length"]
}

def main() -> None:
    
    while True:
        title : str = "PASSWORD MANAGER"
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
        
        
        
        
def ask_fields(choice : str) -> dict:
    
    inputs : dict[str , str] = {}
    
    for field in fields[choices[choice]]:
        input_check = input(f"{field.title()}: ") 
        if input_check.strip() != "":
            inputs[field] = input_check
    
    return inputs
        
    
            
            
def do_option(choice: str) -> None:
        data : dict [str , dict [str , str]] = decode_to_json()
        
        match choice:
            case "1":
                data.update(add_password(ask_fields(choice)))
                encode_to_json(data)
            case "2":
                show_passwords(data)
            case "3":
                result : dict[str , str] = search_password(data,ask_fields(choice))
                
                if result:
                    for key in result:
                                print(f"\nWebsite: {key}")
                                print_fields(data[key])
            case "4":
                encode_to_json(delete_password(data,ask_fields(choice)))
            case "5":
                password : str = genarete_password(ask_fields(choice))
                print(f"\nGenerated Password: {password}")
            case "6":
                encode_to_json(data)
                sys.exit("Good bye!")
        
        input("Press Enter to continue")
            
        
    
if __name__ == "__main__":
    main()