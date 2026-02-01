import taxes_calc as tax


print("Sales Tax Calculator")


def main():
    choice = 'y'
    while choice.lower() == 'y':
        print()
        print("ENTER ITEMS (ENTER 0 TO END)")
        subtotal = 0
        while True:
            item_cost = float(input("Cost of item: "))
            subtotal += item_cost
            if item_cost == 0:
                break
        subtotal = round(subtotal, 2)
        sales_tax_amount = tax.calculate_tax(subtotal)
        total_after_tax = tax.get_total(subtotal)
        print(f"Total:           {subtotal}")
        print(f"Sales tax:       {sales_tax_amount}")
        print(f"Total after tax: {total_after_tax}")
        print()
        choice = input("Again? (y/n) ")
    print()
    print("Thanks, bye!")

    

if __name__ == "__main__":
    main()
