
def welcome():
    print("The Wizard Inventory Program")
    print()



def command_menu():
    print("COMMAND MENU")
    print("show - Show all items")
    print("grab - Grab an item")
    print("edit - Edit an item")
    print("drop - Drop an item")
    print("exit - Exit program")
    print()
    

def show_items(item_list):
    for i, item in enumerate(item_list, start=1):
        print(f"{i}. {item}")



def grab_item(item_list):
    if len(item_list) == 4:
        print("You can't carry anymore items.")
    else:
        new_item = input("Name: ")
        item_list.append(new_item)
        print(f"{new_item} was added.")



def edit_item(item_list):
    item_number = int(input("Number: "))
    if item_number > 4:
        print("Enter a valid item number.")
    else:
        item_index = item_number - 1
        if item_list[item_index] in item_list:
            new_name = input("Updated name: ")
            item_list[item_index] = new_name        
            print(f"Item number {item_number} was updated")



def drop_item(item_list):
    item_number = int(input("Number: "))
    if item_number > 4:
        print("Enter a valid item number.")
    else:
        item_index = item_number - 1
        removal = item_list[item_index]
        item_list.remove(removal)
        print(f"{removal} was dropped.")


def main():

    wizard_items = ['wooden staff', 'wizard hat', 'book of spells']

    welcome()
    command_menu()

    menu_choice = input("Command: ")

    if menu_choice.lower() == 'show':
        show_items(wizard_items)
    elif menu_choice.lower() == 'grab':
        grab_item(wizard_items)
    elif menu_choice.lower() == 'edit':
        edit_item(wizard_items)
    elif menu_choice.lower() == 'drop':
        drop_item(wizard_items)
    
    



if __name__ == "__main__":
    main()
