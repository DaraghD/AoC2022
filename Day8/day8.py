file1 = open("input.txt")
line1 =file1.readline()
line1.rstrip("\n")
leng = len(line1) - 1
file1.close()

row = leng
col = leng
map = [[0 for col in range(col)] for row in range(row)] #creates map

with open("input.txt") as file:
    for x, line in enumerate(file):
        line = line.rstrip("\n")
        for col in range(leng):
            map[x][col] = int(line[col]) # fills in map with tree vals


visible_trees = 0
def treeup(pos:tuple,map:list[list])-> bool:
    row,col = pos
    tree = map[row][col]
    while row > 0:
        row -=1
        if map[row][col] > tree or tree == map[row][col]:
            return False
        else:
            continue
    return True

def treeleft(pos:tuple,map:list[list])-> bool:
    row, col = pos
    tree = map[row][col]
    while col > 0 :
        col -= 1
        if map[row][col] > tree or tree == map[row][col]:
            return False
        else:
            continue
    return True

def treedown(pos:tuple,map:list[list])-> bool:
    row, col = pos
    tree = map[row][col]
    while row < 98:
        row += 1
        if map[row][col] > tree or tree == map[row][col]:
            return False
        else:
            continue
    return True

def treeright(pos:tuple,map:list[list])-> bool:
    row, col = pos
    tree = map[row][col]
    while col < 98:
        col += 1
        if map[row][col] > tree or tree == map[row][col]:
            return False
        else:
            continue
    return True

def tree_check(pos:tuple,map:list[list]):
    if treeright(pos,map) or treeleft(pos,map) or treeup(pos,map) or treedown(pos,map):
        return True
    else:
        return False

for row in range(leng):
    for col in range(leng):
        if row == 0 or col == 0 or col == leng-1 or row == leng-1:
            visible_trees += 1
        elif tree_check((row,col),map):
            visible_trees += 1


print(f"visible_trees : {visible_trees}")
