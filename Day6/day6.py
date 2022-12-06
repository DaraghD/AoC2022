with open("input.txt") as file:
    for line in file:
        temp = []
        for i in range(0,len(line)):
            temp.append(line[i])
            if len(temp) == 14: # 4
                if len(list(set(temp))) == 14: #4
                    print(i+1)
                    break
                else:
                    temp.pop(0)

