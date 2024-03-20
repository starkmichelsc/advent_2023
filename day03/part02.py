from template.util import parse_lines


def execute(filename: str) -> int:
    lines = parse_lines(filename)
    for line in lines:
        print(line)
    return 0
