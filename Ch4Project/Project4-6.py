
print("Prime Number Checker")


def get_int(number):
    if number <= 0 or number > 5000:
        return False


def check_prime(number):
    factors = 0
    for value in range(1, number + 1):
        remainder = (number % value)
        if remainder == 0:
            factors += 1
    return factors
    


def main():
    choice = 'y'
    while choice.lower() == 'y':
        print()
        user_input = int(input("Please enter an integer between 1 and 5000: "))
        check_input = get_int(user_input)
        if check_input == False:
            print("Invalid integer. Please try again.")
        else:
            get_factors = check_prime(user_input)
            if get_factors <= 2:
                print(f"{user_input} is a prime number.")
            else:
                print(f"{user_input} is NOT a prime number.")
                print(f"It has {get_factors} factors.")
        print()
        choice = input("Try again? (y/n): ")
    print()
    print("Bye!")
        

if __name__ == "__main__":
    main()
