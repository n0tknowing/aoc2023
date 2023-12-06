lines = open("01.txt", "r").read().strip().split("\n")
result = 0
digits = []
for line in lines:
    for i in range(len(line)):
        ch = line[i]
        if ch.isdigit():
            digits.append(ch)
        elif ch == "o":
            if line[i:i+3] == "one":
                digits.append("1")
        elif ch == "t":
            if line[i:i+3] == "two":
                digits.append("2")
            elif line[i:i+5] == "three":
                digits.append("3")
        elif ch == "f":
            if line[i:i+4] == "four":
                digits.append("4")
            elif line[i:i+4] == "five":
                digits.append("5")
        elif ch == "s":
            if line[i:i+3] == "six":
                digits.append("6")
            elif line[i:i+5] == "seven":
                digits.append("7")
        elif ch == "e":
            if line[i:i+5] == "eight":
                digits.append("8")
        elif ch == "n":
            if line[i:i+4] == "nine":
                digits.append("9")
    if len(digits) < 2:
        digits.append(digits[0])
    result += 10 * int(digits[0]) + int(digits[-1])
    digits.clear()
print(result)
