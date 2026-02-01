
import csv

def print_menu():
    print("COMMAND MENU")
    print("monthly - View monthly sales")
    print("yearly - View yearly summary")
    print("edit - Edit sales for a month")
    print("exit - Exit program")
    print()


def get_monthly_sales():
    monthly_sales = []
    with open("monthly_sales.csv", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            monthly_sales.append(row)
    return monthly_sales


def view_monthly_sales(monthly_sales):
    for row in monthly_sales:
        print(f"{row[0]} - {row[1]}")


def view_yearly_summary(monthly_sales):
    yearly_total = 0
    for row in monthly_sales:
        row[1] = int(row[1])
        yearly_total += row[1]
    monthly_average = yearly_total / len(monthly_sales)
    print(f"Yearly total:        {yearly_total}")
    print(f"Average sales:       {monthly_average}")


def edit_sales(monthly_sales):
    edit_month = input("Three-letter month: ")
    for row in monthly_sales:
        if row[0] == edit_month:
            new_sales = int(input("Sales amount: "))
            row[1] = new_sales


def update_monthly_sales(monthly_sales):
    with open("monthly_sales.csv", "w", newline = "") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(monthly_sales)


def main():
    monthly_sales = get_monthly_sales()
    print_menu()
    print()

    while True:
        command = input("Command: ")
        print()
        if command == "monthly":
            view_monthly_sales(monthly_sales)
            print()
        elif command == "yearly":
            view_yearly_summary(monthly_sales)
            print()
        elif command == "edit":
            edit_sales(monthly_sales)
            print()
        elif command == "exit":
            break
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()