from main import (
    parse_game,
    total_power_of_fewest_number_of_cubes_in_games,
    fewest_required_number_of_cubes_each_color,
    power_of_fewest_required_colors,
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

def test_fewest_required_number_of_cubes_each_color():
    assert fewest_required_number_of_cubes_each_color({
        'game': 1,
        'blue': [3, 6],
        'green': [2, 2],
        'red': [4, 1],
    }) == {
        'game': 1,
        'blue': 6,
        'green': 2,
        'red': 4,
    }

    assert fewest_required_number_of_cubes_each_color({
        'game': 2,
        'blue': [1, 4, 1],
        'green': [2, 3, 1],
        'red': [1],
    }) == {
        'game': 2,
        'blue': 4,
        'green': 3,
        'red': 1,
    }

    assert fewest_required_number_of_cubes_each_color({
        'game': 3,
        'blue': [6, 5],
        'green': [8, 13, 5],
        'red': [20, 4, 1],
    }) == {
        'game': 3,
        'blue': 6,
        'green': 13,
        'red': 20,
    }

    assert fewest_required_number_of_cubes_each_color({
        'game': 4,
        'blue': [6, 15],
        'green': [1, 3, 3],
        'red': [3, 6, 14],
    }) == {
        'game': 4,
        'blue': 15,
        'green': 3,
        'red': 14,
    }

    assert fewest_required_number_of_cubes_each_color({
        'game': 5,
        'blue': [1, 2],
        'green': [3, 2],
        'red': [6, 1],
    }) == {
        'game': 5,
        'blue': 2,
        'green': 3,
        'red': 6,
    }

def test_power_of_fewest_required_colors():
    assert power_of_fewest_required_colors({
        'game': 1,
        'blue': 6,
        'green': 2,
        'red': 4,
    }) == 48

    assert power_of_fewest_required_colors({
        'game': 2,
        'blue': 4,
        'green': 3,
        'red': 1,
    }) == 12

    assert power_of_fewest_required_colors({
        'game': 3,
        'blue': 6,
        'green': 13,
        'red': 20,
    }) == 1560

    assert power_of_fewest_required_colors({
        'game': 4,
        'blue': 15,
        'green': 3,
        'red': 14,
    }) == 630

    assert power_of_fewest_required_colors({
        'game': 5,
        'blue': 2,
        'green': 3,
        'red': 6,
    }) == 36

def test_total_power_of_fewest_number_of_cubes_in_games():
    text = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''

    assert total_power_of_fewest_number_of_cubes_in_games(text) == 2286

def test_total_power_of_fewest_number_of_cubes_in_games_puzzle_input():
    text = ''
    with open('games.txt', 'r') as file:
        text = file.read()

    assert total_power_of_fewest_number_of_cubes_in_games(text) == 74804
