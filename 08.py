import math

lines = open("08.txt", "r").read().strip().split("\n")
instr = lines[0]
maps = dict()
p2_start = []
for i in range(2, len(lines)):
    l, r = lines[i].split(" = ")
    nd1, nd2 = r.replace("(", "").replace(")", "").split(", ")
    maps[l.strip()] = (nd1.strip(), nd2.strip())
    if l.strip()[-1] == "A":
        p2_start.append(l.strip())
ii = 0
p1 = 0
node = "AAA"
while True:
    ins = instr[ii % len(instr)]
    node = maps[node][0] if ins == "L" else maps[node][1]
    p1 += 1
    if node == "ZZZ":
        break
    ii += 1

ii = 0
p2 = 0
p2_a = []
for st in p2_start:
    ii = 0
    p2 = 0
    while True:
        ins = instr[ii % len(instr)]
        st = maps[st][0] if ins == "L" else maps[st][1]
        p2 += 1
        if st[-1] == "Z":
            break
        ii += 1
    p2_a.append(p2)

p2 = math.lcm(*p2_a)
print(p1, p2)
