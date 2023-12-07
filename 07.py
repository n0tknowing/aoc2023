# set part2 to True in check_type() and compare_label() to get answer for part 2

types = []
for i in range(7):
    types.append([])

def check_type(hand, part2 = False):
    hs = dict()
    for h in hand:
        if h in hs:
            hs[h] += 1
        else:
            hs[h] = 1
    if part2 and "J" in hs:
        high = sorted(hs, key=lambda x: hs[x], reverse=True)
        if high[0] == "J":
            if hs["J"] == 5:
                return 6
            else:
                hs[high[1]] += hs["J"]
        else:
            hs[high[0]] += hs["J"]
        hs.pop("J")
    if len(hs) == 5: # high card
        return 0
    elif len(hs) == 4: # one pair
        return 1
    elif len(hs) == 3: # two pair(2) or three of kind(3)
        has_three = False
        for _,v in hs.items():
            if v == 3:
                has_three = True
        return 2 if not has_three else 3
    elif len(hs) == 2: # full house(4) or four of kind(5)
        has_four = False
        for _,v in hs.items():
            if v == 4:
                has_four = True
        return 4 if not has_four else 5
    else: # five of kind
        return 6

def compare_label(label1, label2, part2 = False):
    label_strength = {"A":14, "K":13, "Q":12, "J":11 if not part2 else 1, "T":10,
                      "9":9, "8":8, "7":7, "6":6, "5":5, "4":4,
                      "3":3, "2":2}
    for i in range(5):
        if label_strength[label1[i]] > label_strength[label2[i]]:
            return 1
        elif label_strength[label1[i]] < label_strength[label2[i]]:
            return -1
    return 0

lines = open("07.txt", "r").read().strip().split("\n")

for line in lines:
    cards, bid = line.split()
    bid = int(bid)
    types[check_type(cards)].append((cards, bid))

temp = []

for i in range(len(types)):
    if len(types[i]) == 0:
        continue
    elif len(types[i]) == 1:
        temp.append(types[i][0])
        continue
    for j in range(len(types[i])):
        for k in range(j+1, len(types[i])):
            if compare_label(types[i][j][0], types[i][k][0]) == 1:
                types[i][j], types[i][k] = types[i][k], types[i][j]
    temp += types[i]

ans = 0
rank = 1
for hand in temp:
    ans += hand[1] * rank
    rank += 1
print(ans)
