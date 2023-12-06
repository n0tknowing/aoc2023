lines = open("02", "r").read().strip().split("\n")
game = 1
p1 = 0
p2 = 0
for line in lines:
    red = 0
    blue = 0
    green = 0
    bag = line[line.index(":") + 2:].split(";")
    for cube in bag:
        cube2 = cube.strip().split(", ")
        for c in cube2:
            ncube, color = c.split(" ")
            if color == "red":
                red = max(red, int(ncube))
            elif color == "green":
                green = max(green, int(ncube))
            else:
                blue = max(blue, int(ncube))
    if red <= 12 and green <= 13 and blue <= 14:
        p1 += game
    p2 += red * green * blue
    game += 1
print(p1, p2)
