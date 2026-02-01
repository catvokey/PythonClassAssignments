

def main():
    with open("rules.txt", newline="") as infile:
        for line in infile:
            print(line, end="")
        print()


if __name__ == "__main__":
    main()
