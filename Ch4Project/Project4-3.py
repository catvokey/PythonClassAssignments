
import conversion as con


def title():
    print("Feet and Meters Conversion")
    print()

title()


def main():
    choice = 'y'
    while choice.lower() == 'y':
        print("Conversions Menu:")
        print("a. Feet to Meters")
        print("b. Meters to Feet")
        menu_choice = input("Select a conversion (a/b) ")
        if menu_choice.lower() == 'a':
            print()
            feet = float(input("Enter feet: "))
            conversion_feet = con.feet_to_meters(feet)
            print(f"{conversion_feet} meters")
        elif menu_choice.lower() == 'b':
            print()
            meters = float(input("Enter meters: "))
            conversion_meters = con.meters_to_feet(meters)
            print(f"{conversion_meters} feet")            
        print()
        choice = input("Would you like to perform another conversion? (y/n) ")

    print()
    print("Thanks, bye!")



if __name__ == "__main__":
    main()
