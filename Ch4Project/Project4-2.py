def print_title():
    print("Hike Calculator")
    print()

print_title()


def miles_to_feet(miles):
    return int(miles * 5280)



def main():
    get_input = float(input("How many miles did you walk? "))
    conversion = miles_to_feet(get_input)
    print(f"You walked {conversion} feet.")



if __name__ == "__main__":
    main()
