def parseInput():
    lst1 = []
    lst2 = []
    with open("input/d1") as f:
        input = [line.strip() for line in f.readlines()]
        for line in input:
            a, b = line.split()
            lst1.append(int(a))
            lst2.append(int(b))
        return lst1, lst2


def p1():
    lst1, lst2 = parseInput()
    lst1.sort()
    lst2.sort()
    total = 0
    for a, b in zip(lst1, lst2):
        total += abs(a - b)
    return total


def p2():
    lst1, lst2 = parseInput()
    map = {}
    for item in lst2:
        val = map.get(item)
        if val is None:
            map[item] = 1
        else:
            map[item] = val + 1

    simScore = 0
    for item in lst1:
        val = map.get(item)
        if val is not None:
            simScore += val * item
    return simScore


print(p2())
