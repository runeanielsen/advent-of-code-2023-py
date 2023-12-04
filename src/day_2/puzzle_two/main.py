import re
from functools import reduce

def parse_game(game):
    matches = re.findall(r'Game \d+|\d+ [a-z]+', game)

    game_info = {
        'game': int(matches[0].split(' ')[-1]),
        "red": [],
        "green": [],
        "blue": [],
    }

    for round in matches[1:]:
        count, color = round.split(' ')
        game_info[color].append(int(count))

    return game_info

def fewest_required_number_of_cubes_each_color(game_info):
    return {
        'game': game_info['game'],
        'red': sorted(game_info['red'])[-1],
        'green': sorted(game_info['green'])[-1],
        'blue': sorted(game_info['blue'])[-1],
    }

def power_of_fewest_required_colors(fewest_required):
    return (fewest_required['red'] *
            fewest_required['green'] *
            fewest_required['blue'])

def total_power_of_fewest_number_of_cubes_in_games(text):
    return reduce(
        lambda acc, fewest_required: acc + power_of_fewest_required_colors(fewest_required),
        map(fewest_required_number_of_cubes_each_color, map(parse_game, text.splitlines())),
        0
    )
