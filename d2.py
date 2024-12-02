def parse_input():
    with open("input/d2") as f:
        return [[int(x) for x in line.strip().split()] for line in f.readlines()]


def p1():
    return sum([1 for line in parse_input() if checkline(line)])


def checkline(line):
    prev = 0
    isIncreasing = line[0] < line[1]
    safe = True
    for num in line:
        if prev == 0:
            prev = num
            continue
        if not (prev != num and abs(prev - num) < 4 and (prev < num) == isIncreasing):
            safe = False
        prev = num
    return safe


def p2():
    return sum(
        any(
            checkline(line[0:i] + line[i+1:])
            for i in range(len(line))
        )
        for line in parse_input()
    )


print(p2())
