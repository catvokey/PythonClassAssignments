import pickle

def write_bird_counter(bird_counter):
    with open('bird_counter.bin', 'wb') as file:
        pickle.dump(bird_counter, file)

def read_bird_counter():
    with open('bird_counter.bin', 'rb') as file:
        bird_counter = pickle.load(file)
        return bird_counter

def display_birds(bird_counter):
    sorted_birds = list(bird_counter.keys())
    sorted_birds.sort()
    print("Name\t\t\t\tCount")
    print("=================== =====")
    for key in sorted_birds:
        print(f"{key}\t\t\t\t{bird_counter[key]}")

def main():
    print("Bird Counter Program")
    print()
    print("Enter 'x' to exit")
    print()

    bird_counter = read_bird_counter()

    while True:
        bird_name = input("Enter name of bird: ")
        if bird_name == "x":
            break
        elif bird_name not in bird_counter:
            bird_counter[bird_name] = 1
        else:
            bird_counter[bird_name] += 1
    print()
    display_birds(bird_counter)

    write_bird_counter(bird_counter)











if __name__ == "__main__":
    main()