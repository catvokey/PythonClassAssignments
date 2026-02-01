
import csv

def read_champion_file():
    champions = {}
    with (open("world_cup_champions.txt", newline="") as csvfile):
        reader = csv.reader(csvfile)
        for line in reader:
            country = line[1]
            years = []
            year = line[0]
            if country not in champions:
                champions[country] = years
                years.append(year)
            else:
                years = champions[country]
                years.append(year)
    return champions


def display_wins(champions):

    print("Country            Wins     Years")
    print("=======            ====     =====")

    sorted_champions = list(champions.keys())
    sorted_champions.sort()
    for key in sorted_champions:
        years = champions[key]
        year_string = ""
        wins = len(champions[key])
        for year in years:
            year_string += str(year) + ", "
        if key == sorted_champions[0]:
            print(f"{key}\t\t\t{wins}\t\t{year_string}")
        else:
            print(f"{key}\t\t\t\t{wins}\t\t{year_string}")



def main():
    champions = read_champion_file()

    display_wins(champions)



if __name__ == "__main__":
    main()