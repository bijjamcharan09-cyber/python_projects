import ast

FILENAME = "contacts.txt"


def load_contacts():
    contacts = []

    try:
        with open(FILENAME, "r") as file:
            for line in file:
                contacts.append(ast.literal_eval(line.strip()))
    except FileNotFoundError:
        pass

    return contacts


def save_contacts(contacts):
    with open(FILENAME, "w") as file:
        for contact in contacts:
            file.write(str(contact) + "\n")


def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    contact = {
        "name": name,
        "phone": phone
    }

    contacts.append(contact)
    save_contacts(contacts)

    print("Contact added successfully.")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    for i, contact in enumerate(contacts):
        print(f"{i + 1}. Name = {contact['name']} \n")
        print(f"   Phone number = {contact['phone']}\n")


def search_contact(contacts):
    name = input("Enter name to search: ").lower()

    found = False

    for contact in contacts:
        if contact["name"].lower() == name:
            print(contact)
            found = True

    if not found:
        print("Contact not found.")


def update_contact(contacts):
    name = input("Enter contact name to update: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            contact["phone"] = input("Enter new phone number: ")
            save_contacts(contacts)
            print("Contact updated successfully.")
            return

    print("Contact not found.")


def delete_contact(contacts):
    name = input("Enter contact name to delete: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully.")
            return

    print("Contact not found.")


def main():
    contacts = load_contacts()

    while True:
        print("\n===== Contact Book =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            view_contacts(contacts)

        elif choice == "3":
            search_contact(contacts)

        elif choice == "4":
            update_contact(contacts)

        elif choice == "5":
            delete_contact(contacts)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


main()
