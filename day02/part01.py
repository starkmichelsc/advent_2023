from day02.util import parse_lines, get_game


def execute(filename: str) -> int:
    lines = parse_lines(filename)

    total = 0
    for line in lines:
        game = get_game(line)
        if game.is_possible():
            print(f"Game {game.number} is possible")
            total += game.number

    return total
