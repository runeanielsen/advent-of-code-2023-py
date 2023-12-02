from main import (
    sum_of_possible_games,
    parse_game,
    is_possible_game
)

def test_parse_game():
    assert parse_game('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green') == {
        'game': 1,
        'blue': [3, 6],
        'green': [2, 2],
        'red': [4, 1],
    }

    assert parse_game('Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue') == {
        'game': 2,
        'blue': [1, 4, 1],
        'green': [2, 3, 1],
        'red': [1],
    }

    assert parse_game('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red') == {
        'game': 3,
        'blue': [6, 5],
        'green': [8, 13, 5],
        'red': [20, 4, 1],
    }

    assert parse_game('Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red') == {
        'game': 4,
        'blue': [6, 15],
        'green': [1, 3, 3],
        'red': [3, 6, 14],
    }

    assert parse_game('Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green') == {
        'game': 5,
        'blue': [1, 2],
        'green': [3, 2],
        'red': [6, 1],
    }

def test_is_possible_game():
    assert is_possible_game({
        'game': 1,
        'blue': [3, 6],
        'green': [2, 2],
        'red': [4, 1],
    })

    assert is_possible_game ({
        'game': 2,
        'blue': [1, 4, 1],
        'green': [2, 3, 1],
        'red': [1],
    })

    assert not is_possible_game ({
        'game': 3,
        'blue': [6, 5],
        'green': [8, 13, 5],
        'red': [20, 4, 1],
    })

    assert not is_possible_game ({
        'game': 4,
        'blue': [6, 15],
        'green': [1, 3, 3],
        'red': [3, 6, 14],
    })

    assert is_possible_game ({
        'game': 5,
        'blue': [1, 2],
        'green': [3, 2],
        'red': [6, 1],
    })

def test_sum_of_possible_games():
    text = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''

    assert sum_of_possible_games(text) == 8

def test_sum_of_possible_games_puzzle_input():
    text = ''
    with open('games.txt', 'r') as file:
        text = file.read()

    assert sum_of_possible_games(text) == 2317
