lines = open("09.txt").read().strip().split("\n")

def solve(a):
    res = 0
    while True:
        if all(i == 0 for i in a):
            break
        b = []
        for i in range(len(a)-1):
            b.append(a[i+1]-a[i])
        res += a[-1]
        a = b
    return res

p1 = 0
p2 = 0
for line in lines:
    line = [int(i) for i in line.split()]
    p1 += solve(line)
    line.reverse()
    p2 += solve(line)
print(p1, p2)
