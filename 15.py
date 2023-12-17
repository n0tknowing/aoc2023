import re

def do_hash(line):
    r = 0
    for ch in line:
        r = (r + ord(ch)) * 17 % 256
    return r

lines = open("15.txt", "r").read().strip().split(",")
boxes = dict()
p1, p2 = 0, 0

for line in lines:
    focal = re.split("[=-]", line)
    label = focal[0]
    lense = int(focal[1]) if focal[1].isdigit() else None
    box = do_hash(label)
    opr = line[line.find(label) + len(label)]
    if opr == "=":
        if box in boxes:
            boxes[box][label] = lense
        else:
            boxes[box] = dict()
            boxes[box][label] = lense
    else:
        if box in boxes:
            if label in boxes[box]:
                boxes[box].pop(label)
                if len(boxes[box]) == 0:
                    boxes.pop(box)
    p1 += do_hash(line)

p2 = 0
for k, v in boxes.items():
    i = 1
    j = k + 1
    for _, x in v.items():
        p2 += j * i * x
        i += 1

print(p1, p2)
