import random as rd
import string as st
import pyperclip

def get_userappname(): #This function prompts the user to enter a userappname and returns it.
    userappname = input("Enter userappname: ")
    return userappname

def get_username(): #This function prompts the user to enter a username and returns it.
    username = input("Enter username: ")
    return username
def get_password_options(): #This function prompts the user to enter password options and returns them.
    length = int(input("Enter password length: "))

    include_numbers = input("Include numbers? (yes/no): ").lower()

    include_symbols = input("Include symbols? (yes/no): ").lower()

    password_count = int(input("How many passwords do you want to generate? "))

    return length, include_numbers, include_symbols, password_count
def generate_password(length, include_numbers, include_symbols): #This function generates a password based on the specified options and returns it.

    characters = st.ascii_letters

    password = [
        rd.choice(st.ascii_uppercase),
        rd.choice(st.ascii_lowercase)
    ]

    if include_numbers == "yes":
        characters += st.digits
        password.append(rd.choice(st.digits))

    if include_symbols == "yes":
        characters += st.punctuation
        password.append(rd.choice(st.punctuation))

    while len(password) < length:
        password.append(rd.choice(characters))

    rd.shuffle(password)

    return "".join(password)

def check_strength(password):

    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for char in password:

        if char.isupper():
            has_upper = True

        elif char.islower():
            has_lower = True

        elif char.isdigit():
            has_digit = True

        elif char in st.punctuation:
            has_symbol = True

    if len(password) >= 12 and has_upper and has_lower and has_digit and has_symbol:
        return "Strong"

    elif len(password) >= 8 and has_upper and has_lower:
        return "Medium"

    else:
        return "Weak"

def save_to_file(userappname, username, password, strength):

    file = open("passwords.txt", "a")

    file.write(f"{userappname}:{username} : {password} ({strength})\n")

    file.close()
def display_password(userappname, username, password, strength):

    print("\n----- Password Details -----")
    print("Userappname :", userappname)
    print("Username :", username)
    print("Password :", password)
    print("Strength :", strength)

def view_saved_passwords():
    try:
        with open("passwords.txt", "r") as file:
            print("\n----- Saved Passwords -----\n")

            count = 1

            for line in file:
                line = line.strip()

                if not line:
                    continue  # Skip blank lines

                parts = line.split(":")

                if len(parts) < 3:
                    print(f"Invalid entry: {line}")
                    continue

                appname = parts[0].strip()
                username = parts[1].strip()
                password = parts[2].split(" (")[0].strip()
                strength = parts[2].split("(")[1].replace(")", "")

                print(f"{count}. App Name : {appname}")
                print(f"   Username : {username}")
                print(f"   Password : {password}")
                print(f"   Strength : {strength}\n")

                count += 1

    except FileNotFoundError:
        print("No saved passwords found.")

def delete_saved_password():
    userappname = input("Enter useapprname to delete: ").lower()

    found = False

    with open("passwords.txt", "r") as file:
        lines = file.readlines()

    with open("passwords.txt", "w") as file:
        for line in lines:
            saved_app = line.split(":")[0].lower()

            if saved_app != userappname:
                file.write(line)
            else:
                found = True

    if found:
        print("Password(s) deleted successfully.")
    else:
        print("Username not found.")

def copy_to_clipboard(text):
    try:
        pyperclip.copy(text)
        print("-"*20)
        print("Password copied to clipboard.")
        print("-"*20)
    except Exception as e:
        print("-"*20)
        print("Error copying to clipboard:",e)
        print("-"*20)

def ask_and_copy(password):
    choice = input("Copy password to clipboard? (yes(y)/no(n)): ").lower()

    if choice == "yes" or choice == "y":
        copy_to_clipboard(password)
    else:
        print("-"*20)
        print("Copy skipped.")
        print("-"*20)


def copy_saved_password():
    try:
        with open("passwords.txt", "r") as file:
            lines = file.readlines()

        if not lines:
            print("No saved passwords found.")
            return

        print("\n----- Saved Passwords -----")

        for i, line in enumerate(lines, start=1):
            line = line.strip()

            if not line:
                continue

            parts = line.split(":")

            if len(parts) < 3:
                print(f"Invalid entry: {line}")
                continue

            appname = parts[0].strip()
            username = parts[1].strip()

            print(f"{i}. App: {appname} | Username: {username}")

        index = int(input("\nEnter password index: "))

        if 1 <= index <= len(lines):
            line = lines[index - 1]
            password = line.split(":")[2].split(" (")[0].strip()

            pyperclip.copy(password)

            print("-" * 20)
            print("Password copied to clipboard.")
            print("-" * 20)

        else:
            print("Invalid index.")

    except FileNotFoundError:
        print("No saved passwords found.")

    except ValueError:
        print("Please enter a valid number.")

def main():

   while True:
        
        print("\n----- Password Generator -----")
        print("1. Generate Password")
        print("2. View Saved Passwords")
        print("3. Delete Saved Password")
        print("4. Copy to clipboard")
        print("5. Copy saved passwords")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            userappname = get_userappname()
            username = get_username()
            length, include_numbers, include_symbols, password_count = get_password_options()

            for _ in range(password_count):
                password = generate_password(length, include_numbers, include_symbols)
                strength = check_strength(password)
                display_password(userappname, username, password, strength)
                save_to_file(userappname, username, password, strength)
                ask_and_copy(password)
        elif choice == "2":
            view_saved_passwords()
        elif choice == "3":
            delete_saved_password()
        
        elif choice == "4":
              if password:
                 ask_and_copy(password)
              else:
                 print("Generate a password first.")
        elif choice == "5":
            copy_saved_password()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted.")