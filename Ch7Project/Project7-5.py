import csv


def compile_list():
    contact_list = []
    with open("prospects.csv", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            contact_list.append(row)
    return contact_list


def change_case(contact_list):
    for contact in contact_list:
        contact[0] = contact[0].strip().title()
        contact[1] = contact[1].strip().title()
        contact[2] = contact[2].strip().lower()


def write_clean_file(contact_list):
    with open("prospects_clean.csv", "w", newline = "") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(contact_list)


def main():
    print("Welcome to the Email List Cleaner")
    print()
    contact_list = compile_list()
    change_case(contact_list)
    print("Source list:   prospects.csv")
    print("Cleaned list:  prospects_clean.csv")
    print()
    write_clean_file(contact_list)
    print("Congratulations! Your list has been cleaned.")



if __name__ == "__main__":
    main()