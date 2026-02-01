import csv

def print_menu():
    print("Contact Manager")
    print()
    print("COMMAND MENU")
    print("list - Display all contacts")
    print("view - View a contact")
    print("add - Add a contact")
    print("del - Delete a contact")
    print("exit - Exit program")
    print()


def get_contacts():
    contacts = []
    with open('contacts.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            contacts.append(row)
    return contacts


def list_contacts(contact_list):
    for i, contact in enumerate(contact_list, start=1):
        print(f"{i}. {contact[0]}")
    print()

def view_contact(contact_list):
    number = int(input("Number: "))
    if number < 1 or number > len(contact_list):
        print("Invalid contact number.")
        print()
    else:
        contact = contact_list[number - 1]
        print(f"Name: {contact[0]}")
        print(f"Email: {contact[1]}")
        print(f"Number: {contact[2]}")
        print()


def add_contact(contact_list):
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    new_contact = [name, email, phone]
    contact_list.append(new_contact)
    print(f"{new_contact[0]} was added.")
    print()


def delete_contact(contact_list):
    number = int(input("Number: "))
    if number < 1 or number > len(contact_list):
        print("Invalid contact number.")
        print()
    else:
        contact = contact_list.pop(number - 1)
        print(f"{contact[0]} was deleted.")
        print()


def update_contact_list(contact_list):
    with open("contacts.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(contact_list)


def main():
    contact_list = get_contacts()
    print_menu()

    while True:
        command = input("Command: ")
        if command == "list":
            list_contacts(contact_list)
        elif command == "view":
            view_contact(contact_list)
        elif command == "add":
            add_contact(contact_list)
            update_contact_list(contact_list)
        elif command == "del":
            delete_contact(contact_list)
            update_contact_list(contact_list)
        elif command == "exit":
            print("Bye!")
            break


if __name__ == "__main__":
    main()