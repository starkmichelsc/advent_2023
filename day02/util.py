from shlex import join
from typing import List, Tuple

CUBES = {"red": 12, "green": 13, "blue": 14}


class Cube:
    def __init__(self, color: str, number: int):
        self.color = color
        self.number = number

    def __eq__(self, other):
        if not isinstance(other, Cube):
            return False

        return self.color == other.color and self.number == other.number

    def __str__(self):
        return f"Cube: {self.color} {self.number}"

    color: str
    number: int


class Round:
    def __init__(self, cubes: List[Cube]):
        self.cubes = cubes

    def __eq__(self, other):
        if not isinstance(other, Round):
            return False
        return self.cubes == other.cubes

    def __str__(self):
        return f"Round: {join([str(c) for c in self.cubes])}"

    cubes: List[Cube]



class Game:
    def __init__(self, number: int, rounds: List[Round]):
        self.number = number
        self.rounds = rounds

    def __eq__(self, other):
        if not isinstance(other, Game):
            return False
        return self.number == other.number and self.rounds == other.rounds

    def is_possible(self) -> bool:
        for r in self.rounds:
            for c in r.cubes:
                if c.number > CUBES[c.color]:
                    return False
        return True

    number: int
    rounds: List[Round]


def parse_lines(filename: str) -> List[str]:
    result = []
    with open(filename, "r") as file:
        for line in file:
            result.append(line.strip())
    return result


def get_game(val: str) -> Game:
    text = val.split(":")
    rounds = get_rounds(text[1])
    number = int(text[0].split(" ")[1])
    return Game(number, rounds)


def get_rounds(val: str) -> List[Round]:
    round_txt = val.split(';')
    rounds = []
    for r in round_txt:
        rounds.append(Round(get_cubes(r)))
    return rounds


def get_cubes(val: str) -> List[Cube]:
    cube_txt = val.split(',')
    cubes = []
    for c in cube_txt:
        vals = c.strip().split(' ')
        cubes.append(Cube(vals[1], int(vals[0])))

    return cubes
