print("Even or Odd Checker")
print()


def even_or_odd(number):
    check = number % 2
    if check == 0:
        return True
    else:
        return False
    


def main():
    user_input = int(input("Enter an integer: "))
    print()
    result = even_or_odd(user_input)
    if result == False:
        print("This is an odd number.")
    else:
        print("This is an even number.")
    


if __name__ == "__main__":
    main()


