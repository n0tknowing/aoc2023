def solve(time, distance):
    tm = 0
    win = 0
    while tm <= time:
        if tm * (time - tm) > distance:
            win += 1
        tm += 1
    return win

lines = open("06.txt", "r").read().strip().split("\n")
times = [int(i) for i in lines[0][lines[0].index(":") + 2:].split()]
distances = [int(i) for i in lines[1][lines[1].index(":") + 2:].split()]
p1_a = []

for i in range(len(times)):
    time = times[i]
    distance = distances[i]
    p1_a.append(solve(time, distance))

p1 = p1_a[0]
for p in range(1, len(p1_a)):
    p1 *= p1_a[p]

print(p1)

p2_time = int(lines[0][lines[0].index(":") + 2:].replace(" ", ""))
p2_distance = int(lines[1][lines[1].index(":") + 2:].replace(" ", ""))
p2 = solve(p2_time, p2_distance)
print(p2)
