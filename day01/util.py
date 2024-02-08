from typing import List


def parse_values(nums: List[str]) -> int:
    first = int(nums[0])
    second = int(nums[len(nums) - 1]) if len(nums) > 1 else int(nums[0])

    return (first * 10) + second


def parse_lines(filename: str) -> List[str]:
    result = []
    with open(filename, "r") as file:
        for line in file:
            result.append(line.strip())
    return result
