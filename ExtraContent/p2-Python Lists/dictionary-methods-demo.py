'''
    player 1: 
        id           => 1
        name         => Cristiano Ronaldo
        yearOfBirth  => 1985
        nationality  => Portugal
        current_team => Portugal
        history      => Juventus,Real Madrid,Portugal

    player 2: 
        id           => 2
        name         => Lionel Messi
        yearOfBirth  => 1987
        nationality  => Argentina
        current_team => Barcelona
        history      => Barcelona,Argentina,Portugal
'''

# 1- Store the given information in a dictionary.

players = {
    '1': {
            'name': 'Cristiano Ronaldo',
            'yearOfBirth': '1985',
            'nationality': 'Portugal',
            'current_team': 'Portugal',
            'history': ['Juventus', 'Real Madrid', 'Portugal']
        },
    '2': {
            'name': 'Lionel Messi',
            'yearOfBirth': '1987',
            'nationality': 'Argentina',
            'current_team': 'Barcelona',
            'history': ['Barcelona', 'Argentina', 'Portugal']
        }
}

# To add new player information

# id = input('Player ID: ')
# name = input('Player name: ')
# nationality = input("Country: ")
# yearOfBirth = input('Year of birth: ')
# current_team = input('Current team: ')
# history = input('Playing history (comma-separated): ')

# players.update({
#     id: {
#         "name": name,
#         "yearOfBirth": yearOfBirth,
#         "nationality": nationality,
#         "current_team": current_team,
#         "history": history.split(',')
#     }
# })

# Repeat the above code block to add another player if needed.


# 2- Search for a player by ID.
# id = input('Enter the player ID to search: ')
# player = players.get(id)
# print(f'name: {player.get("name")}')

# 3- Delete a player record by ID.

id = input('Enter the player ID to delete: ')
players.pop(id)

print(players)
