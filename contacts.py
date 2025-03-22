contacts = []

def validate_phone(phone):
    if phone.startswith("+") and phone[1:].isdigit() and 9 <= len(phone) <= 13:
        return True
    elif phone.isdigit() and 9 <= len(phone) <= 13:
        return True
    else:
        print("Error: Invalid phone number format! (Example: +998901234567)")
        return False

def validate_email(email):
    if "@" in email and "." in email.split("@")[1] and len(email.split("@")[0]) > 0:
        return True
    else:
        print("Error: Invalid email format! (Example: example@gmail.com)")
        return False

def add_contact():
    print("\n=== Add New Contact ===")
    name = input("Name: ")

    phone = input("Phone number: ")
    while not validate_phone(phone):
        phone = input("Phone number: ")

    email = input("Email address: ")
    while not validate_email(email):
        email = input("Email address: ")

    address = input("Address: ")
    new_contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(new_contact)
    print("Contact successfully added!\n")

def update_contact():
    print("\n=== Update Contact ===")
    search = input("Enter the name or phone number of the contact to update: ")
    for contact in contacts:
        if contact["name"] == search or contact["phone"] == search:
            print("Contact found: ", contact)

            new_name = input(f"New name (current: {contact['name']}): ") or contact["name"]

            new_phone = input(f"New phone (current: {contact['phone']}): ") or contact["phone"]
            while new_phone != contact["phone"] and not validate_phone(new_phone):
                new_phone = input("New phone: ")

            new_email = input(f"New email (current: {contact['email']}): ") or contact["email"]
            while new_email != contact["email"] and not validate_email(new_email):
                new_email = input("New email: ")

            new_address = input(f"New address (current: {contact['address']}): ") or contact["address"]

            contact.update({"name": new_name, "phone": new_phone, "email": new_email, "address": new_address})
            print("Contact successfully updated!\n")
            return

    print("Contact not found!\n")

def delete_contact():
    print("\n=== Delete Contact ===")
    search = input("Enter the name or phone number of the contact to delete: ")
    for contact in contacts:
        if contact["name"] == search or contact["phone"] == search:
            contacts.remove(contact)
            print("Contact successfully deleted!\n")
            return
    print("Contact not found!\n")

def search_contact():
    print("\n=== Search Contact ===")
    search = input("Enter the name or phone number of the contact to search: ")
    for contact in contacts:
        if contact["name"] == search or contact["phone"] == search:
            print("Contact found: ", contact)
            return
    print("Contact not found!\n")

def list_all_contacts():
    print("\n=== All Contacts ===")
    if not contacts:
        print("The contact list is empty!\n")
    else:
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact}")

def menu():
    while True:
        print("\n=== Contact Book ===")
        print("1. Add New Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. Show All Contacts")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            update_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            search_contact()
        elif choice == "5":
            list_all_contacts()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    menu()
