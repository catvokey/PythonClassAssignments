TAX_RATE = 0.06


def calculate_tax(cost):
    tax = round(cost * TAX_RATE, 2)
    return tax


def get_total(cost):
    total = round(cost + calculate_tax(cost), 2)
    return total


def main():
    check_sales = calculate_tax(50)
    check_total = get_total(50)
    print(f"Taxes = {check_sales} Total = {check_total}")

    

if __name__ == "__main__":
    main()
