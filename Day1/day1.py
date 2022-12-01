inputlist :list[str] = []
sumlist:list[int] = []

with open("input.txt", 'r') as file:
    for line in file:
        line = line.rstrip('\n')
        inputlist.append(line)

counter = 0
for i in range(0,len(inputlist),1):
    if inputlist[i] == '':
        sumlist.append(counter)
        counter = 0
    else:
        counter += int(inputlist[i])

print(sumlist)
print(max(sumlist))
