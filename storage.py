import json
import sys
from pathlib import Path


path = Path("passwords.json")

def encode_to_json(data) -> None:
    with path.open("w") as file:
        json.dump(data, file, indent=2)
        


def decode_to_json() -> dict:
    if path.exists():
        with path.open("r") as file:
            data = json.load(file)
            return data
    else:
        return {}
    