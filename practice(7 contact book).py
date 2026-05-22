contacts = []


def add_contact():
    name = input("Name: ")
    phone = input("Phone number: ")
    email = input("Email: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })
    print(f"Contact '{name}' added successfully!")


def view_contacts():
    if not contacts:
        print("No contacts found")
    else:
        for i, c in enumerate(contacts, 1):
            print(f"{i}. {c['name']} - {c['phone']} - {c['email']}")


def search_contact():
    query = input("Enter name to search: ").lower()
    results = []

    for c in contacts:
        if query in c['name'].lower():
            results.append(c)

    if results:
        print("Search results:")
        for i, c in enumerate(results, 1):
            print(f"{i}. {c['name']} - {c['phone']} - {c['email']}")
    else:
        print("No contacts found.")


def remove_contact():
    view_contacts()
    if not contacts:
        return

    while True:
        try:
            num = int(input("Enter the number of the contact to remove: "))
            if 1 <= num <= len(contacts):
                break
            else:
                print(f"Enter a number between 1 and {len(contacts)}.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    removed = contacts.pop(num - 1)
    print(f"Contact '{removed['name']}' removed successfully")


def edit_contact():
    view_contacts()
    if not contacts:
        return

    while True:
        try:
            num = int(input("Enter the number of the contact to edit: "))
            if 1 <= num <= len(contacts):
                break
            else:
                print(f"Enter a number between 1 and {len(contacts)}.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    c = contacts[num - 1]

    print(f"Editing contact '{c['name']}' - press Enter to keep current value")

    name = input(f"Name [{c['name']}]: ")
    phone = input(f"Phone [{c['phone']}]: ")
    email = input(f"Email [{c['email']}]: ")

    if name:
        c['name'] = name
    if phone:
        c['phone'] = phone
    if email:
        c['email'] = email

    print("Contact updated successfully")


print("Welcome to the contact book!")

if __name__ == '__main__':
    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Remove Contact")
        print("5. Edit Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            remove_contact()
        elif choice == "5":
            edit_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-6.")
