lines = open("04.txt", "r").read().strip().split("\n")
p1 = 0
p2 = len(lines) * [1]

for i in range(len(lines)):
    card = lines[i][lines[i].index(":") + 2:].strip()
    wins, nums = card.split(" | ")
    wins = set(wins.strip().split())
    nums = set(nums.strip().split())
    matches = len(wins.intersection(nums))
    if matches > 0:
        p1 += 2 ** (matches - 1)
        for j in range(i+1, i+matches+1):
            p2[j] += p2[i]

print(p1, sum(p2))
