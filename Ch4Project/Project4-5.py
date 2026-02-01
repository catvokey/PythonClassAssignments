import random

print("Dice Roller")


def get_roll():
    result = random.randint(1, 6)
    return result


def main():
        print()
        user_choice = input("Roll the dice? (y/n): ")
        while user_choice.lower() == 'y':
            roll_result_1 = get_roll()
            roll_result_2 = get_roll()
            roll_total = roll_result_1 + roll_result_2
            print()
            print(f"Die 1: {roll_result_1}")
            print(f"Die 2: {roll_result_2}")
            print(f"Total: {roll_total}")
            if roll_result_1 == 1 and roll_result_2 == 1:
                print("Snake eyes!")
            elif roll_result_1 == 6 and roll_result_2 == 6:
                print("Boxcars!")
            print()
            user_choice = input("Roll again? (y/n) ")

 


if __name__ == "__main__":
    main()
