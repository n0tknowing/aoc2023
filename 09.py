lines = open("09.txt").read().strip().split("\n")

def solve(a):
    a2 = []
    if all(i == 0 for i in a):
        return 0
    for i in range(len(a)-1):
        a2.append(a[i+1]-a[i])
    return a[-1] + solve(a2)

p1 = 0
p2 = 0
for line in lines:
    line = [int(i) for i in line.split()]
    p1 += solve(line)
    line.reverse()
    p2 += solve(line)
print(p1, p2)
