alphabet:str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
total:int = 0
with open("input.txt") as file:
    for line in file:
        common:list[chr] = []
        line = line.rstrip('\n')
        rucksack1:str = line[0:int((len(line) /2))]
        rucksack2:str = line[int((len(line) /2)):len(line)]
        for char in rucksack1:
            if rucksack2.find(char) != -1:
                if char not in common:
                    common.append(char)
                    total += (alphabet.index(char) +1)

print(total)
#part 2
inputlist:list[str] = []
with open("input.txt") as file:
    for line in file:
        line = line.rstrip('\n')
        inputlist.append(line)

total2:int = 0
for i in range(0,len(inputlist),3):
    elf1:str = inputlist[i]
    elf2:str = inputlist[i+1]
    elf3:str = inputlist[i+2]
    for char in elf1:
        if char in elf2 and char in elf3:
            total2 += alphabet.index(char) + 1
            break

print(total2)