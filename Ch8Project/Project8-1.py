
def calculate_total(tip, meal_cost):
    total = meal_cost + tip
    return total

def calculate_tip(tip_percentage, meal_cost):
    tip_percentage = tip_percentage / 100
    tip_amount = round(meal_cost * tip_percentage, 2)
    return tip_amount

def main():
    print("Tip Calculator")
    print()

    while True:
        try:
            meal_cost = float(input("Cost of meal: "))
            if meal_cost <= 0:
                print("Must be greater than 0. Please try again.")
                continue
            else:
                break
        except ValueError:
            print("Must be a valid decimal number. Please try again.")
            continue
    while True:
        try:
            tip_percentage = int(input("Tip percent: "))
            tip_amount = calculate_tip(tip_percentage, meal_cost)
            total = calculate_total(tip_amount, meal_cost)
            break
        except ValueError:
            print("Must be a valid integer. Please try again.")

    print()
    print(f"Cost of meal: {meal_cost}")
    print(f"Tip percent:  {tip_percentage}")
    print(f"Tip amount:   {tip_amount}")
    print(f"Total amount: {total}")




if __name__ == "__main__":
    main()