import json

# Load contacts from a file if it exists, otherwise initialize an empty dictionary
def load_contacts(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save contacts to a file
def save_contacts(contacts, filename):
    with open(filename, 'w') as file:
        json.dump(contacts, file)

# Add a new contact
def add_contact(contacts):
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")

    contacts[name] = {'phone': phone, 'email': email}
    print("Contact added successfully!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

# Edit an existing contact
def edit_contact(contacts):
    name = input("Enter the name of the contact to edit: ")
    if name in contacts:
        print("Current Contact Information:")
        print(f"Name: {name}, Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")

        phone = input("Enter the new phone number (press enter to keep current): ")
        email = input("Enter the new email address (press enter to keep current): ")

        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email

        print("Contact updated successfully!")
    else:
        print("Contact not found.")

# Delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

# Main program loop
def main():
    filename = 'contacts.json'
    contacts = load_contacts(filename)

    while True:
        print("\nContact Management System")
        print("1. Add a new contact")
        print("2. View all contacts")
        print("3. Edit an existing contact")
        print("4. Delete a contact")
        print("5. Quit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            save_contacts(contacts, filename)
            print("Contacts saved. Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
