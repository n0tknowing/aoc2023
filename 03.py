import string

p1, p2 = 0, 0
digits = set()
lines = open("e.txt", "r").read().strip().replace(".", " ").split("\n")

def add_digit(line, dx, sets):
    beg, end = dx, dx
    while beg > 0 and line[beg - 1].isdigit():
        beg -= 1
    while end < len(line) and line[end].isdigit():
        end += 1
    sets.add(int(line[beg:end]))

for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] in string.punctuation:
            digits.clear()
            y_beg = y - 1 if y > 0 else y
            y_end = y + 1 if y < len(lines) - 1 else y
            x_beg = x - 1 if x > 0 else x
            x_end = x + 1 if x < len(lines[y]) - 1 else x
            for dy in range(y_beg, y_end + 1):
                for dx in range(x_beg, x_end + 1):
                    if dy == y and dx == x:
                        continue
                    if lines[dy][dx].isdigit():
                        add_digit(lines[dy], dx, digits)
            print(lines[y][x], digits)
            p1 += sum(digits)
            if lines[y][x] == "*" and len(digits) == 2:
                gear_1, gear_2 = digits
                p2 += gear_1 * gear_2

print(p1, p2)
