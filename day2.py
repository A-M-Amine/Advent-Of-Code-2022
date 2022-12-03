
def gameScore(path):

    with open(path, "r") as guide:

        TotalscorePart1 = 0
        TotalscorePart2 = 0

        for round in guide.readlines():
            
            round = round.strip()

            if round != "": 
                playersChoices = round.split(" ")
            
                TotalscorePart1 += roundOutcome(playersChoices[0],playersChoices[1])
                TotalscorePart2 += definedroundOutcome(playersChoices[0],playersChoices[1])

    print("part 1: ", TotalscorePart1)
    print("part 2: ", TotalscorePart2)


def roundOutcome(choice1, choice2):

    deck = { 'X': ('A',1,'B'), 'Y': ('B',2,'C'), 'Z': ('C',3,'A') }

    
    #   Draw
    if choice1 == deck[choice2][0]:
        return deck[choice2][1] + 3
    #   Win
    if choice1 != deck[choice2][2]:
        return deck[choice2][1] + 6
    #   lost
    return deck[choice2][1]


def definedroundOutcome(choice1, choice2):

    deck = { 'A': ('X','Y'), 'B': ('Y','Z'), 'C': ('Z','X') }

    # generate win
    if choice2 == 'Z':
        return roundOutcome(choice1, deck[choice1][1])
    # generate draw
    if choice2 == 'Y':
        return roundOutcome(choice1, deck[choice1][0])
    # generate loss
    choices = ['X','Y','Z']
    losingChoice = [i for i in choices if i not in deck[choice1]]
    return roundOutcome(choice1, losingChoice[0])


gameScore("input.txt")