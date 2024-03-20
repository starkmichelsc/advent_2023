from functools import reduce
from operator import mul

from day02.util import parse_lines, get_game


def execute(filename: str) -> int:
    lines = parse_lines(filename)

    total = 0

    for line in lines:

        min_vals = {'red': 0, 'green': 0, 'blue': 0}
        game = get_game(line)
        print(f"Game {game.number}")
        for round in game.rounds:
            print(f"\t{round}")
            for cube in round.cubes:
                if cube.number > min_vals[cube.color]:
                    min_vals[cube.color] = cube.number
                    print(f"\t\tmin_vals: {min_vals}")
        total += reduce(mul, min_vals.values())
        print(f"\t\ttotal: {total}")

    return total
