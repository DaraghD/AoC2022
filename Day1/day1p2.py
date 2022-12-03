inputlist:list[str] = []
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
top3list: list[int] = []
for i in range(0,3,1):
    maxindex = sumlist.index(max(sumlist))
    top3list.append(max(sumlist))
    sumlist.pop(maxindex)

print(top3list)
print(sum(top3list))

