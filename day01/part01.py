from util import parse_values, parse_lines


def execute(filename: str) -> int:
    lines = parse_lines(filename)
    vals = []
    for line in lines:
        nums = []
        for char in line:
            if char.isdigit():
                nums.append(char)

        val = parse_values(nums)
        vals.append(val)

    return sum(vals)
