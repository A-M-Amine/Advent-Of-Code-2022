# part 1
def getMaxCalories(path):

    data = [i.strip() for i in open(path, "r").readlines()]

    maxcals = 0
    caloriesCount = 0

    for val in data:
        if val != '':
            caloriesCount += int(val)
        else:
            maxcals = max(maxcals,caloriesCount)
            caloriesCount = 0
        

    if caloriesCount != 0:
        maxcals = max(maxcals,caloriesCount)


    return maxcals


# part 2 
def topThreeCals(path):

    data = [i.strip() for i in open(path, "r").readlines()]

    sumOfCals = []
    caloriesCount = 0

    for val in data:
        if val != '':
            caloriesCount += int(val)
        else:
            sumOfCals.append(caloriesCount)
            caloriesCount = 0
        
    if caloriesCount != 0:
        sumOfCals.append(caloriesCount)

    sumOfCals.sort(reverse=True)

    return sum(sumOfCals[:3])




print(topThreeCals("input.txt"))