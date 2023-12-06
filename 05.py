def solve(seed, trange):
    loc = seed
    for (dst, src, length) in trange:
        if src <= seed and seed < src + length:
            loc = seed + dst - src
    return loc

lines = open("05.txt", "r").read().strip().split("\n")
seeds_p1 = [int(i) for i in lines[0][lines[0].index(":") + 2:].split()]
seeds_p2 = []

for i in range(0, len(seeds_p1), 2):
    start = seeds_p1[i]
    length = seeds_p1[i+1]
    for k in range(start, start+length):
        seeds_p2.append(k)

maps = []
j = 0

for i in range(2, len(lines)):
    if len(lines[i]) == 0:
        j += 1
        continue
    if lines[i].find("map:") != -1:
        maps.append([])
        continue
    dst, src, length = [int(i) for i in lines[i].split()]
    maps[j].append((dst, src, length))

tseeds = [seeds_p1, seeds_p2]
p1, p2 = [], []

for i in range(len(tseeds)):
    for seed in tseeds[i]:
        for m in maps:
            seed = solve(seed, m)
        if i == 0:
            p1.append(seed)
        else:
            p2.append(seed)

print(min(p1), min(p2))
