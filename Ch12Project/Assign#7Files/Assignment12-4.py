
import csv

def read_sales():
    monthly_sales = {}
    with open('monthly_sales.txt') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            month = row[0]
            sales = row[1]
            monthly_sales[month] = sales
    return monthly_sales

def write_sales(monthly_sales):
    with open('monthly_sales.txt', 'w', newline="") as csvfile:
        writer = csv.writer(csvfile)
        for month, sales in monthly_sales.items():
            writer.writerow([month, sales])

def command_menu():
    print("COMMAND MENU")
    print("view   - View sales for specified month")
    print("edit   - Edit sales for specified month")
    print("totals - View sales summary for year")
    print("exit   - Exit program")
    print()

def view_sales(monthly_sales):
    month = input("Three-letter Month: ")
    month = month.title()
    if month in monthly_sales:
        sales = monthly_sales[month]
        print(f"Sales amount for {month} is {sales}.00.")
    else:
        print("Invalid three-letter month.")

def edit_sales(monthly_sales):
    month = input("Three-letter Month: ")
    month = month.title()
    if month in monthly_sales:
        sales = int(input("Sales Amount: "))
        monthly_sales[month] = sales
        print(f"Sales amount for {month} is {sales}.00.")

def get_total(monthly_sales):
    total = 0
    for month in monthly_sales.items():
        sales = int(month[1])
        total += sales
    return total

def get_average(total, monthly_sales):
    average = round(total / len(monthly_sales), 2)
    return average

def main():
    print("Monthly Sales Program")
    print()
    monthly_sales = read_sales()
    command_menu()
    while True:
        choice = input("Command: ")
        if choice == "view":
            view_sales(monthly_sales)
            print()
        elif choice == "edit":
            edit_sales(monthly_sales)
            write_sales(monthly_sales)
            print()
        elif choice == "totals":
            total = get_total(monthly_sales)
            average = get_average(total, monthly_sales)
            print(f"Yearly total:             {total}.00")
            print(f"Average sales amount:      {average}")
            print()
        elif choice == "exit":
            break
        else:
            print("Invalid choice. Try again.")
            print()
    print()
    print("Bye!")


if __name__ == "__main__":
    main()