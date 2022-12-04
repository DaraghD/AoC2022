def bounds(inputline: str) -> tuple[int, int, int, int]:
    x = inputline.split(',')
    id1 = x[0]
    id2 = x[1]
    firstid = id1.split('-')
    secondid = id2.split('-')
    return int(firstid[0]), int(firstid[1]), int(secondid[0]), int(secondid[1])

def overlap_fun(idtpl:tuple)-> int:
    if idtpl[1] >= idtpl[2] and idtpl[3] >= idtpl[0]:
        return 1

    return 0

overlap = 0
with open("input.txt") as file:
    for line in file:
        line = line.rstrip('\n')
        idtuple = bounds(line)
        if idtuple[0] <= idtuple[2] and idtuple[1] >= idtuple[3]:
            overlap += 1
        elif idtuple[2] <= idtuple[0] and idtuple[3] >= idtuple[1]:
            overlap += 1

#print(overlap)

#part2
total = 0
with open("input.txt") as file:
    for line in file:
        line = line.rstrip('\n')
        total += overlap_fun(bounds(line))

print(total)
