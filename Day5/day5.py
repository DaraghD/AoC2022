crate_dict = {1: ['D','T','W','F','J','S','H','N'],
              2: ['H','R','P','Q','T','N','B','G'],
              3: ['L','Q','V'],
              4: ['N','B','S','W','R','Q'],
              5: ['N','D','F','T','V','M','B'],
              6: ['M','D','B','V','H','T','R'],
              7: ['D','B','Q','J'],
              8: ['D','N','J','V','R','Z','H','Q'],
              9: ['B','N','H','M','S']}

with open("input.txt") as file:
    for line in file:
        line = line.rstrip('\n')
        line = [int(x) for x in line if x.isdigit()]
        if len(line) == 4:
            steps = int(str(line[0])+str(line[1]))
            crate1 = line[2]
            crate2 = line[3]
        else:
            steps = line[0]
            crate1 =line[1]
            crate2=line[2]
        temp_crate = []

        for i in range(steps):
            x = crate_dict[crate1].pop()
            temp_crate.append(x)
            #crate_dict[crate2].append(x)
        temp_crate.reverse()
        for crate in temp_crate:
            crate_dict[crate2].append(crate)

for i in range(1,10):
    print(crate_dict[i][-1])
