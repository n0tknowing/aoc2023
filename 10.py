import sys

lines = open(sys.argv[1]).read().strip().split("\n")
seen = set()
grid = dict()
S = (-1,-1)
Q = []

def pipes(y, x):
    ch = grid[(y, x)]
    if ch == "|":
        return [(y - 1, x), (y + 1, x)]
    elif ch == "-":
        return [(y, x - 1), (y, x + 1)]
    elif ch == "L":
        return [(y - 1, x), (y, x + 1)]
    elif ch == "J":
        return [(y - 1, x), (y, x - 1)]
    elif ch == "7":
        return [(y + 1, x), (y, x - 1)]
    elif ch == "F":
        return [(y + 1, x), (y, x + 1)]
    else:
        assert(0)

for y in range(len(lines)):
    for x in range(len(lines[y])):
        grid[(y, x)] = lines[y][x]
        if lines[y][x] == "S":
            S = (y, x)
            if x < len(lines[y]) - 1 and lines[y][x + 1] in ("-", "L", "F"):
                Q.append((y, x + 1)) # right/east
            if y < len(lines) - 1 and lines[y + 1][x] in ("|", "7", "F"):
                Q.append((y + 1, x)) # bottom/south
            if x > 0 and lines[y][x - 1] in ("-", "J", "7"):
                Q.append((y, x - 1)) # left/west
            if y > 0 and lines[y - 1][x] in ("|", "L", "J"):
                Q.append((y - 1, x)) # top/north

p1 = 0
seen.add(S)

while len(Q) > 0:
    p1 += 1
    (y, x) = Q.pop()
    for pipe in pipes(y, x):
        if pipe in grid and grid[pipe] != "." and pipe not in seen:
            seen.add(pipe)
            Q.append(pipe)

print(p1 // 2)
