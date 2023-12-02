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

def is_possible_game(game_info):
    possible_max_value_red = 12;
    possible_max_value_green = 13;
    possible_max_value_blue = 14;

    return (
        all(count <= possible_max_value_red for count in game_info['red']) and
        all(count <= possible_max_value_green for count in game_info['green']) and
        all(count <= possible_max_value_blue for count in game_info['blue'])
    )

def sum_of_possible_games(text):
    return reduce(
        lambda acc, value: acc + value['game'],
        filter(is_possible_game, map(parse_game, text.splitlines())),
        0
    )
