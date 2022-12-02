#A ROCK - B PAPER - C SCISSORS
#X ROCK - Y PAPER - Z SCISSORS - what i play

#SCORE = SHAPE +  OUT COME,   ROCK = 1, PAPER = 2, 3 = SCISSORS , OUTCOMES = 0 LOSE, 3 DRAW , 6 WON

inputlist = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.rstrip("\n")
        inputlist.append(line)

print(inputlist[1][0])
if inputlist[1][2] == 'Y':
    print(1)
score = 0
for i in range(0,len(inputlist)):
    match inputlist[i][0]:
        case 'A':#ROCK
            match inputlist[i][2]:
                case 'X': #lose
                    score += 3
                case 'Y':#draw
                    score += 4
                case 'Z':#WIN
                    score += 8
        case 'B':#PAPER
            match inputlist[i][2]:
                case 'X':#lose
                    score += 1
                case 'Y':#draw
                    score += 5
                case 'Z':#WIN
                    score += 9
        case 'C':#SCISSORS
            match inputlist[i][2]:
                case 'X':#lose
                    score += 2
                case 'Y':#draw
                    score += 6
                case 'Z':#WIN
                    score += 7



print(score)