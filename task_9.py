import json
import os

CONTACTS_FILE = "contacts.json"

# Load contacts from file if exists
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

# Add contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print(f"Contact {name} added successfully!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']} - {contact['email']}")

# Search contact
def search_contact(contacts):
    keyword = input("Enter name or phone to search: ").lower()
    results = [c for c in contacts if keyword in c['name'].lower() or keyword in c['phone']]
    
    if results:
        print("Search results:")
        for c in results:
            print(f"{c['name']} - {c['phone']} - {c['email']}")
    else:
        print("No contact found.")

# Delete contact
def delete_contact(contacts):
    name = input("Enter the name of contact to delete: ").lower()
    for c in contacts:
        if c['name'].lower() == name:
            contacts.remove(c)
            print(f"Contact {c['name']} deleted successfully!")
            return
    print("Contact not found.")

# Main program loop
def main():
    contacts = load_contacts()
    
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print("Contacts saved. Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
