
def command_menu():
    print("COMMAND MENU")
    print("list - Display all contacts")
    print("view - View a contact")
    print("add - Add a contact")
    print("del - Delete a contact")
    print("exit - Exit program")
    print()


def display_contacts(contact_list):
    for i, contact in enumerate(contact_list, start=1):
        print(f"{i}. {contact[0]}") 


def view_contact(contact_list):
    number = int(input("Number: ")) 
    if number < 1 or number > len(contact_list):
        print("Invalid contact number.")
    else:
        contact = contact_list[number - 1]
        print(f"Name: {contact[0]}")
        print(f"Email: {contact[1]}")
        print(f"Number: {contact[2]}")
        

def add_contact(contact_list):
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    new_contact = [name, email, phone]
    contact_list.append(new_contact)
    print(f"{new_contact[0]} was added.")


def delete_contact(contact_list):
    number = int(input("Number: "))
    if number < 1 or number > len(contact_list):
        print("Invalid contact number.")
    else:
        contact = contact_list.pop(number-1)
        print(f"{contact[0]} was deleted.")



def main():
    contact_list = [['Bob Robertson', 'bobbob@email.com', 7095551234],
                    ['Steve Stevenson', 'stevesteve@email.com', 7095554321],
                    ['Patrick Fitzpatrick', 'patpatrick@email.com', 7095555678],
                    ['Donald McDonald', 'donmcdon@email.com', 7095558765]]

    command_menu()

    user_choice = input("Command: ")

    if user_choice == 'list':
        display_contacts(contact_list)

    elif user_choice == 'view':
        view_contact(contact_list)


    elif user_choice == 'add':
        add_contact(contact_list)


    elif user_choice == 'del':
        delete_contact(contact_list)


    elif user_choice == 'exit':
        print("Bye!")    



if __name__ == "__main__":
    main()
