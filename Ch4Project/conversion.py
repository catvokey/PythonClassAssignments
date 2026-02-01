


def feet_to_meters(feet):
    meters = round(feet * 0.3048, 2)
    return meters


def meters_to_feet(meters):
    feet = round(meters / 0.3048, 2)
    return feet



def main():
    test_meters = feet_to_meters(20)
    test_feet = meters_to_feet(20)
    print(f"Feet to meters: {test_meters} Meters to feet: {test_feet}")


if __name__ == "__main__":
    main()
