file1 = open("input.txt")
line1 =file1.readline()
line1.rstrip("\n")
leng = len(line1) - 1
file1.close()

row = leng
col = leng
map = [[0 for col in range(col)] for row in range(row)]

with open("input.txt") as file:
    for x, line in enumerate(file):
        line = line.rstrip("\n")
        for col in range(leng):
            map[x][col] = int(line[col])

def display_map(map): #debug function
    for row in range(len(map)):
        print(map[row])
        for col in range(len(map[row])):
            if col == len(map[row]):
                print("\n")
                continue


def treeup(pos:tuple,map:list[list])-> int:
    row,col = pos
    row1 = row
    tree = map[row][col]
    while row > 0:
        row -=1
        if map[row][col] > tree or tree == map[row][col]:
            return abs(row1-row)
    return abs(row1-row)

def treeleft(pos:tuple,map:list[list])-> int:
    row, col = pos
    col1 = col
    tree = map[row][col]
    while col > 0 :
        col -= 1
        if map[row][col] > tree or tree == map[row][col]:
            return abs(col1-col)
    return abs(col1-col)

def treedown(pos:tuple,map:list[list])-> int:
    row, col = pos
    row1 = row
    tree = map[row][col]
    while row < 98:
        row += 1
        if map[row][col] > tree or tree == map[row][col]:
            return abs(row1-row)

    return abs(row1-98)

def treeright(pos:tuple,map:list[list])-> int:
    row, col = pos
    col1 = col
    tree = map[row][col]
    while col < 98:
        col += 1
        if map[row][col] > tree or tree == map[row][col]: #we bump into tree
            return abs(col1-col)
    return abs(col1 - col)


def tree_calc(pos:tuple,map:list[list]):
    return treeright(pos,map) * treeleft(pos,map)* treeup(pos,map) * treedown(pos,map)

scenic = []

for row in range(leng):
    for col in range(leng):
        scenic.append(tree_calc((row,col),map))


print(f"{max(scenic)}: highest value")
