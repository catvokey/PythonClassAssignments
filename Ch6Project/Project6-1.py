def intro_message():
    print("Prime Number Checker")
    print()

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
    
    
def list_factors(number):
    factors = 0
    factors_list = []
    factors_output = " "
    for value in range(1, number + 1):
        remainder = (number % value)
        if remainder == 0:
            factors += 1
            factors_list.append(value)
    for factor in factors_list:
        factors_output += f"{factor} "
    print(f"It has {factors} factors. {factors_output}")


def main():
    choice = 'y'
    while choice.lower() == 'y':
        #print intro
        intro_message()

        #get user input
        number = int(input("Please enter an integer between 1 and 5000: "))
        print()
        if get_int(number) == False:
            print("Please enter a valid number.")
        else:
            #check if prime
            get_factors = check_prime(number)
            if get_factors <= 2:
                print(f"{number} is a prime number.")
            else:
                print(f"{number} is NOT a prime number.")
                list_factors(number)
                

        print()
        choice = input("Try again? (y/n): ")
        print()

    print("Bye!")


if __name__ == "__main__":
    main()
