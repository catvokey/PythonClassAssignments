

def display_players(players):
    print("ALL PLAYERS:")
    for player in players:
        print(player)


def display_stats(players):
    player_name = input("Enter player name: ")
    player_name = player_name.title()
    if player_name in players:
        player = players[player_name]
        print(f"Wins: {player['wins']}")
        print(f"Losses: {player['losses']}")
        print(f"Ties: {player['ties']}")


def main():

    players = { 'Bob' : { 'wins' : 37, 'losses' : 14, 'ties' : 7},
                'Lisa' : { 'wins' : 39, 'losses' : 10, 'ties' : 9},
                'Carl' : { 'wins' : 42, 'losses' : 8, 'ties' : 6}}

    choice = 'y'
    while choice == 'y':
        display_players(players)
        print()
        display_stats(players)
        print()
        choice = input("Continue? (y/n): ")

    print()
    print("Bye!")



if __name__ == "__main__":
    main()