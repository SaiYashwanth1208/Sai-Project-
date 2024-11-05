import json

def load_contacts(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_contacts(filename, contacts):
    with open(filename, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    contacts[name] = phone
    print(f"Contact {name} added.")

def view_contacts(contacts):
    if contacts:
        print("Contact List:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts found.")

def search_contact(contacts):
    name = input("Enter the name of the contact to search: ")
    phone = contacts.get(name)
    if phone:
        print(f"{name}: {phone}")
    else:
        print(f"Contact {name} not found.")

def contact_book():
    filename = 'contacts.json'
    contacts = load_contacts(filename)

    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            save_contacts(filename, contacts)
            print("Exiting. Contacts saved.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    contact_book()
