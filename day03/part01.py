from template.util import parse_lines

# 514969
# wrong answer
def execute(filename: str) -> int:
    lines = parse_lines(filename)
    coords = []

    for index, line in enumerate(lines):
        coords.append([])
        for i, c in enumerate(line + "."):
            coords[index].append((c, False))
            # print(c)
        # print(line)
    # print(coords)

    for row, y in enumerate(coords):
        for col, x in enumerate(y):
            val = y[col][0]
            if not val.isdigit() or val == '.':
                continue
            # print(f"val: {val}, row: {row}, col: {col}")
            top_left = coords[row - 1][col - 1] if row > 0 and col > 0 else "."
            top = coords[row - 1][col] if row > 0 else "."
            top_right = coords[row - 1][col + 1] if row > 0 and col < len(y) - 1 else "."
            left = coords[row][col - 1] if col > 0 else "."
            right = coords[row][col + 1] if col < len(y) - 1 else "."
            bottom_left = coords[row + 1][col - 1] if row < len(coords) - 1 and col > 0 else "."
            bottom = coords[row + 1][col] if row < len(coords) - 1 else "."
            bottom_right = coords[row + 1][col + 1] if row < len(coords) - 1 and col < len(y) - 1 else "."


            if not top_left[0].isdigit() and top_left[0] != '.':
                y[col] = (y[col][0],True)
            elif not top[0].isdigit() and top[0] != '.':
                y[col] = (y[col][0],True)
            elif not top_right[0].isdigit() and top_right[0] != '.':
                y[col] = (y[col][0], True)
            elif not left[0].isdigit() and left[0] != '.':
                y[col] = (y[col][0], True)
            elif not right[0].isdigit() and right[0] != '.':
                y[col] = (y[col][0], True)
            elif not bottom_left[0].isdigit() and bottom_left[0] != '.':
                y[col] = (y[col][0], True)
            elif not bottom[0].isdigit() and bottom[0] != '.':
                y[col] = (y[col][0], True)
            elif not bottom_right[0].isdigit() and bottom_right[0] != '.':
                y[col] = (y[col][0],True)


            print(f"""
|{top_left[0]:^5}{top[0]:^5}{top_right[0]:^5}|
|{left[0]:^5}{y[col][0]:^5}{right[0]:^5}| {y[col][1]}
|{bottom_left[0]:^5}{bottom[0]:^5}{bottom_right[0]:^5}|
""")

            coords[row][col] = y[col]
    print(coords)
    nums = []

    for row, y in enumerate(coords):
        a_num = ""
        is_part_number = False

        for col, x in enumerate(y):
            if x[1]:
                is_part_number = True
            if x[0].isdigit():
                a_num += x[0]

            else:
                nums.append((a_num, is_part_number))
                a_num = ""
                is_part_number = False
            # if a_num.isdigit() and col == len(y) - 1:
            #     nums.append((a_num, is_part_number))

            print(f"{a_num} {is_part_number}, col: {col}, row: {row}, len: {len(y)}")
    # print()
    # print(nums)
    # print()
    filtered = [t for t in nums if t[0] != ""]
    # print(filtered)
    total = [int(t[0]) for t in filtered if t[1] == True]
    # total.sort()
    print(total)
    return sum(total)