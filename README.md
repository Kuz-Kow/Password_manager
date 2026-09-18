# Password Manager

A simple command-line password manager written in Python.

This project was created as a learning project to practice Python functions, dictionaries, JSON file handling, modules, the `pathlib`, `random`, and `string` modules, as well as basic project organization.

> **Warning:** This project is educational. Passwords are currently stored in plain text inside a JSON file and should not be used to store real passwords.

## Features

* Add a new password
* Display saved passwords
* Search for a password by website
* Delete a saved password
* Generate random passwords
* Save passwords to a JSON file
* Load passwords from a JSON file
* Validate password length
* Handle missing password database

## Project Structure

```text
password-manager/
│
├── main.py
├── manager.py
├── storage.py
├── generator.py
├── passwords.json
└── tests/
    ├── test_manager.py
    ├── test_storage.py
    └── test_generator.py
```

### `manager.py`

Contains the main password-management functionality:

* `add_password()`
* `show_passwords()`
* `search_password()`
* `print_fields()`
* `delete_password()`

### `storage.py`

Responsible for storing and loading password data.

* `encode_to_json()`
* `decode_to_json()`

### `generator.py`

Contains the password-generation functionality.

* `genarete_password()`

### `main.py`

Provides the command-line interface and connects the different parts of the application.

## Data Format

Passwords are stored in `passwords.json`.

Example:

```json
{
  "github.com": {
    "username": "andrii",
    "password": "example123"
  },
  "gmail.com": {
    "username": "andrii@gmail.com",
    "password": "another_password"
  }
}
```

## How It Works

### Adding a password

The program receives information about a website, username, and password.

```python
{
    "github.com": {
        "username": "andrii",
        "password": "example123"
    }
}
```

The password is displayed as asterisks when it is added:

```text
Website: github.com
Username: andrii
Password: ***********

Password saved
```

### Searching for a password

The program checks whether the requested website exists in the dictionary.

For example:

```text
Website: github.com

Username: andrii
Password: example123
```

If the website does not exist:

```text
No record has been found
```

### Deleting a password

The program checks whether the website exists and removes the corresponding dictionary entry.

```text
Website: github.com

Password for github.com deleted.
```

### Generating a password

The password generator creates a random password using:

* lowercase letters
* uppercase letters
* digits
* punctuation characters

For example:

```text
Password length: 16

x7@Kp2!mQ9#zL4$w
```

The password length is validated before generation.

## Technologies

* Python 3
* JSON
* `pathlib`
* `random`
* `string`

## Python Concepts Practiced

This project was created to practice:

* Functions
* Dictionaries
* Loops
* Conditional statements
* Recursion
* Type hints
* File handling
* JSON serialization/deserialization
* Modules
* Exception handling
* `pathlib`
* Random data generation

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
```

Move into the project directory:

```bash
cd password-manager
```

Run the program:

```bash
python main.py
```

## Future Improvements

Possible improvements for future versions:

* [ ] Add password encryption
* [ ] Add master password authentication
* [ ] Hide passwords when displaying them
* [ ] Add password strength validation
* [ ] Prevent duplicate websites
* [ ] Add password editing
* [ ] Add password copying to clipboard
* [ ] Add automated tests with `pytest`
* [ ] Improve error handling
* [ ] Replace JSON storage with SQLite
* [ ] Add command-line arguments with `argparse`
* [ ] Add logging
* [ ] Create a graphical interface
* [ ] Create a REST API

## Disclaimer

This application is intended for educational purposes only.

Passwords are currently stored as plain text in `passwords.json`. Do not use this application to store real or sensitive passwords.

A production password manager would require proper encryption, secure key management, authentication, and additional security measures.
