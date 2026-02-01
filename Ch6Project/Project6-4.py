
def get_sales(sales):
    q1 = float(input("Enter sales for Q1: "))
    sales.append(q1)
    q2 = float(input("Enter sales for Q2: "))
    sales.append(q2)
    q3 = float(input("Enter sales for Q3: "))
    sales.append(q3)
    q4 = float(input("Enter sales for Q4: "))
    sales.append(q4)

def get_total(sales):
    total = sum(sales)
    total = round(total, 2)
    print(f"Total:              {total}")


def calc_average(sales):
    total = sum(sales)
    average = round(total / 4, 2)
    print(f"Average Quarter:    {average}")


def get_min(sales):
    sales.sort()
    lowest = round(sales[0], 2)
    print(f"Lowest Quarter:     {lowest}")


def get_max(sales):
    sales.sort()
    highest = round(sales[3], 2)
    print(f"Highest Quarter:    {highest}")


def main():
    choice = 'y'
    while choice.lower() == 'y':
        
        sales = []

        print("The Quarterly Sales Program")
        print()

        get_sales(sales)
        print()
        get_total(sales)
        calc_average(sales)
        get_min(sales)
        get_max(sales)

        print()
        choice = input("Would you like to go again? (y/n) ")
        print()

    print("Bye!")


if __name__ == "__main__":
    main()
