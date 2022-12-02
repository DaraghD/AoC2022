with open("input.txt", "r") as file:
    score=0
    for line in file:
        line = line.rstrip("\n")
        match line[0], line[2]:
            case 'A', 'X':
                score += 3
            case 'A', 'Y':
                score += 4
            case 'A', 'Z':
                score += 8
            case 'B', 'X':
                score += 1
            case 'B', 'Y':
                score += 5
            case 'B', 'Z':
                score += 9
            case 'C', 'X':
                score += 2
            case 'C', 'Y':
                score += 6
            case 'C', 'Z':
                score += 7
print(score)
