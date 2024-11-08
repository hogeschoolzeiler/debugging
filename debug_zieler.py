contacts = []

def add_contact(name, phone_numbers, email):
    contact = {
        'name': name,
        'phone_numbers': phone_numbers,
        'email': email
    }
    contacts.append(contact)

def search_contacts(keyword):
    return list(filter(lambda c: keyword.lower() in c['name'].lower() or keyword.lower() in c['email'].lower(), contacts))

def delete_contact(name):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            print(f"Contact {name} deleted successfully.")
            return
    print(f"No contact found with name: {name}")

def update_contact(name, phone_numbers, email):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contact['phone_numbers'] = phone_numbers
            contact['email'] = email
            print(f"Contact {name} updated successfully.")
            return
    print(f"No contact found with name: {name}")

def main():
    add_contact("John Doe", ["1234567890", "9876543210"], "john@example.com")
    add_contact("Jane Smith", ["5555555555"], "jane@example.com")
    add_contact("Bob Johnson", ["1111111111", "2222222222", "3333333333"], "bob@example.com")

    search_term = input("Enter a name or email to search: ")
    search_results = search_contacts(search_term)

    if search_results:
        print("Search Results:")
        for contact in search_results:
            print(f"Name: {contact['name']}")
            print("Phone Numbers:", ', '.join(contact['phone_numbers']))
            print(f"Email: {contact['email']}")
    else:
        print("No matching contacts found.")

    contact_name = input("Enter the name of the contact to delete: ")
    delete_contact(contact_name)

    update_name = input("Enter the name of the contact to update: ")
    update_phone_numbers = input("Enter the new phone numbers (separated by commas): ").split(",")
    update_email = input("Enter the new email address: ")
    update_contact(update_name, update_phone_numbers, update_email)

if __name__ == "__main__":
    main()
