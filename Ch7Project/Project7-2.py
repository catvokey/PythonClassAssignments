
import random

def welcome():
    print("The Wizard Inventory Program")
    print()

def command_menu():
    print("COMMAND MENU")
    print("walk - Walk down the path")
    print("show - Show all items")
    print("drop - Drop an item")
    print("exit - Exit program")
    print()

def get_item_list():
    wizard_all_items = []
    with open("wizard_all_items.txt", "r") as infile: 
        for line in infile:
            line = line.replace("\n", "")
            wizard_all_items.append(line)
    return wizard_all_items


def get_inventory():
    wizard_inventory = []
    with open("wizard_inventory.txt", "r") as infile: 
        for line in infile:
            line = line.replace("\n", "")
            wizard_inventory.append(line)
    return wizard_inventory

    
def get_random_item(wizard_all_items):
    random_item = random.choice(wizard_all_items)
    return random_item    


def check_if_full(wizard_inventory):
    if len(wizard_inventory) == 4:
        return False
    else:
        return True    


def update_inventory(wizard_all_items, wizard_inventory):
    with open("wizard_all_items.txt", "w") as outfile:
        for item in wizard_all_items:
            outfile.write(f"{item}\n")
    with open("wizard_inventory.txt", "w") as outfile:
        for item in wizard_inventory:
            outfile.write(f"{item}\n")


def show_items(item_list):
    for i, item in enumerate(item_list, start=1):
        print(f"{i}. {item}")


def drop_item(wizard_inventory):
    item_number = int(input("Number: "))
    if item_number > 4:
        print("Enter a valid item number.")
    else:
        item_index = item_number - 1
        removal = wizard_inventory[item_index]
        wizard_inventory.remove(removal)
        print(f"{removal} was dropped.")


def main():
    wizard_all_items = get_item_list()
    wizard_inventory = get_inventory()

    welcome()
    command_menu()

    while True:
        command = input("Command: ")

        if command.lower() == "walk":
            random_item = get_random_item(wizard_all_items)
            print(f"While walking down a path, you see {random_item}.")
            choice = input("Do you want to grab it? (y/n) ")

            if choice.lower() == 'y':
                check = check_if_full(wizard_inventory)
                if check == True:
                    wizard_inventory.append(random_item)
                    wizard_all_items.remove(random_item)
                    print(f"You picked up {random_item}.")
                else:
                    print("Your pockets are full. Drop something if you want different items.")

            update_inventory(wizard_all_items, wizard_inventory)

        elif command.lower() == "show":
            show_items(wizard_inventory)

        elif command.lower() == "drop":
            drop_item(wizard_inventory)
            update_inventory(wizard_all_items, wizard_inventory)

        elif command.lower() == "exit":
            break

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
