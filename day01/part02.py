from util import parse_values, parse_lines

numMap = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def execute(filename: str) -> int:
    lines = parse_lines(filename)
    total_value = 0
    for line in lines:
        nums = []
        for index, char in enumerate(line):
            if char.isdigit():
                nums.append(char)
            else:
                remainder = line[index:]
                for text, num in numMap.items():
                    if remainder.startswith(text):
                        nums.append(num)
                        break
        val = parse_values(nums)

        total_value += val
    return total_value
