def runCrane(path):


    with open(path, "r") as data:

        # seperating input
        stacksData, movesData = data.read().split("\n\n")[:2]
        

        # initializing stacks with a defined size
        size = stacksData.split("\n")[-1][-2]
        stacks = createStacks(int(size))
        stacks2 = createStacks(int(size))

        # populating stacks with input data
        populateStacks(stacks, stacksData.split("\n"))
        populateStacks(stacks2, stacksData.split("\n"))

        # part 1  
        rearrange(movesData.split("\n"), stacks)
        part1 = getResults(stacks)
        
        # part 2
        rearrange2(movesData.split("\n"), stacks2)
        part2 = getResults(stacks2)



        print("part 1 ",part1) 
        print("part 2 ",part2) 


def createStacks(number):

    stacks = []

    for i in range(number):
        stacks.append([])

    return stacks


def populateStacks(stacks, dataS):

    dataS.reverse()
    for line in dataS[1:]:
        cpt = 0
        for ele in range(1,len(line),4):
            if line[ele]!= ' ':
                stacks[cpt].append(line[ele])
            cpt += 1
        

    return stacks


def rearrange(moves, stacks):
    
    for move in moves:
        
        moveinpt = move.split(" ")
        
        for i in range(int(moveinpt[1])):
            ele = stacks[int(moveinpt[3]) - 1].pop()
            stacks[int(moveinpt[5]) - 1].append(ele)



def rearrange2(moves, stacks):
    
    for move in moves:
        
        moveinpt = move.split(" ")
        
        indexold = int(moveinpt[3]) - 1
        indexNew = int(moveinpt[5]) - 1
        size = int(moveinpt[1])

        ele = stacks[indexold][-size:]
        stacks[indexold] = stacks[indexold][:-size]
        stacks[indexNew].extend(ele)


def getResults(stacks):
    res = ""
    for stack in stacks:
        if stack:
            res += stack[-1]


    return res



runCrane("data/input5.txt")