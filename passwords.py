def add_password(fields: dict) -> dict:
    
    print(f"\nWebsite: {fields["website"]}\nUsername: {fields["username"]}\nPassword: {"*"*len(fields["password"])}")
    print("\nPassword saved")
    return {f"{fields["website"]}":{"username":fields["username"], "password":fields["password"]}}
    
    
def show_passwords(data: dict) -> None:
    
    if data:
        for key in data:
            print(f"\nWebsite: {key}")
            print_fields(data[key])
    else:
        print("No passwords added")
        
def search_password(data : dict,fields : dict) -> dict:
    
    if fields["website"] in data:
        return {fields["website"]: data[fields["website"]]}

    else:
        print("No record has been found")
        return {}

def print_fields(fields : dict) -> None:
    for field in fields:
        print(f"{field.title()}: {fields[field]}")

    
def delete_password(data : dict,fields : dict) -> dict:
    
        
    if fields["website"] in data:
        del data[fields["website"]]
        print(f"Password for {fields["website"]} deleted.")
    else:
        print(f"There is no suche a website in passwords")
    
    return data

