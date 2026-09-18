from typing import  Never
from dataclasses import dataclass


type PasswordDict = dict[str, FieldDict]

type FieldDict = dict[str, str]




def add_password(fields: FieldDict) ->PasswordDict:
    '''Adds returns new password to data'''
    print(f"\nWebsite: {fields["website"]}\nUsername: {fields["username"]}\nPassword: {"*"*len(fields["password"])}")
    print("\nPassword saved")
    return {f"{fields["website"]}":{"username":fields["username"], "password":fields["password"]}}
    
    
def show_passwords(data: PasswordDict) -> None:
    '''
    Prints all password in data. 
    If no pass words prints message: "No passwords added"
    '''
    if data:
        for key in data:
            print(f"\nWebsite: {key}")
            print(data[key])
            print_fields(data[key])
    else:
        print("No passwords added")
        
def search_password(data : PasswordDict,fields : FieldDict) -> PasswordDict | dict[Never, Never]:
    '''Searches password through data'''
    if fields["website"] in data:
        return {fields["website"]: data[fields["website"]]}

    else:
        print("No record has been found")
        return {}

def print_fields(fields_to_print : FieldDict) -> None:
    '''Print fields for other funcrtions'''
    for field in fields_to_print:
        print(f"{field.title()}: {fields_to_print[field]}")


def delete_password(data : PasswordDict,fields : FieldDict ) -> PasswordDict:
    '''Delets password from data'''
    if fields["website"] in data:
        del data[fields["website"]]
        print(f"Password for {fields["website"]} deleted.")
    else:
        print("There is no suche a website in passwords")
    
    return data

