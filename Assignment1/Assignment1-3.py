
from dataclasses import dataclass

import csv

@dataclass
class Customer:
    customer_id: str
    firstname: str
    lastname: str
    company: str = ""
    address: str = ""
    city: str = ""
    state: str = ""
    zip: str =""

    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}"

    @property
    def full_address(self):
        if self.company != "":
            return f"{self.address}\n{self.company}\n{self.city} {self.zip}"
        else:
            return f"{self.address}\n{self.city} {self.zip}"

def read_customer_data():
    customer_data = []
    with open("customers.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            customer = Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            customer_data.append(customer)
    customer_data.pop(0)
    return customer_data

def main():
    customer_data = read_customer_data()

    print(customer_data)

    print("Customer Viewer")
    print()

    choice = 'y'
    while choice == 'y':
        get_id = input("Enter customer ID: ")
        found = False
        for customer in customer_data:
            if get_id == customer.customer_id:
                found = True
                print(customer.fullname)
                print(customer.full_address)
                print()
                break
        if found == False:
            print("No customer with that ID.")

        choice = input("Continue? (y/n): ")

    print("Bye!")

if __name__ == "__main__":
    main()