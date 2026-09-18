import json
from pathlib import Path
from passwords import PasswordDict
from typing import Never


path = Path("passwords.json")

def encode_to_json(data : PasswordDict) -> None:
    '''
    Saves files to json file
    '''
    with path.open("w") as file:
        json.dump(data, file, indent=2)
        


def decode_to_json() -> PasswordDict :
    '''
    Decodes data from data and returns it.
    If no data returns holow dict
    '''
    if path.exists():
        with path.open("r") as file:
            data = json.load(file)
            return data
    else:
        return {}
    