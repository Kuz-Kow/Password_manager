def add_password():
    website = input("Website: ")
    username = input("Username: ")
    password = input("Password: ")
    
    if website.strip() != "" and username.strip() != "" and password.strip() != "":
        print(f"\nWebsite: {website}\nUsername: {username}\nPassword: {"*"*len(password)}")
        print("\nPassword saved")
        return {f"{website}":{"username":username, "password":password}}
    
    else:
        print("You didn't entered all fields!")
        return add_password()
    
    
def show_passwords(data):
    
    if data:
        for key in data:
            print(f"\nWebsite: {key}")
            print_fields(data[key])
    else:
        print("No passwords added")
        
def search_password(data):
    website = (input("\nWebsite: ")).strip()
    
    for key in data:
        if key == website:
                print(f"\nWebsite: {key}")
                print_fields(data[key])
                return

        
    print("No record has been found")
    

def print_fields(fields):
    for field in [dictionary for dictionary in fields]:
        print(f"{field.title()}: {fields[field]}")

    
def delete_password(data):
    website = (input("\nWebsite: ")).strip()
    
        
    if website in data:
        del data[website]
        print(f"Password for {website} deleted.")
    else:
        print(f"There is no suche a website in passwords")
    
    return data

