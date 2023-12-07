def solve(time, distance):
    tm = 0
    win = 0
    while tm <= time:
        if tm * (time - tm) > distance:
            win += 1
        tm += 1
    return win

lines = open("06.txt", "r").read().strip().split("\n")
p1_time = [int(i) for i in lines[0][lines[0].index(":") + 2:].split()]
p1_distance = [int(i) for i in lines[1][lines[1].index(":") + 2:].split()]
p2_time = int(lines[0][lines[0].index(":") + 2:].replace(" ", ""))
p2_distance = int(lines[1][lines[1].index(":") + 2:].replace(" ", ""))

p1 = 1
for i in range(len(p1_time)):
    time = p1_time[i]
    distance = p1_distance[i]
    p1 *= solve(time, distance)

p2 = solve(p2_time, p2_distance)
print(p1, p2)
