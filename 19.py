W, R = open("19.txt", "r").read().strip().split("\n\n")
W = W.split("\n")
R = R.split("\n")
workflows = dict()
ratings = []
cats = {"x": 0, "m": 1, "a": 2, "s": 3}

def solve(workflow, rating):
    wf = workflow.split(":")
    cat = cats[wf[0][0]]
    cond = wf[0][1]
    num = int(wf[0][2:])
    dest = wf[-1]
    if cond == ">" and rating[cat] > num:
        accept = True
    elif cond == "<" and rating[cat] < num:
        accept = True
    else:
        accept = False
    return (dest, accept)

for w in W:
    w = w.strip()
    brace = w.find("{")
    part = w[0 : brace]
    workflow = w[brace+1:-1].split(",")
    workflows[part] = workflow

for r in R:
    r = r.strip()
    rating = r[r.find("{")+1:-1].split(",")
    rx = int(rating[0].split("=")[1])
    rm = int(rating[1].split("=")[1])
    ra = int(rating[2].split("=")[1])
    rs = int(rating[3].split("=")[1])
    ratings.append((rx, rm, ra, rs))

p1 = 0
for rating in ratings:
    part = "in"
    while True:
        wf = workflows[part]
        for i in range(len(wf) - 1):
            dest, accept = solve(wf[i], rating)
            if accept:
                part = dest
                break
        if not accept:
            part = wf[-1]
        if part == "A" or part == "R":
            if part == "A":
                p1 += sum(rating)
            break

print(p1)
