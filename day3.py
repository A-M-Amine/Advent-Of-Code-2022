from string import ascii_letters


def rucksackItem(rucksack):

    firstCompartment = set(rucksack[:len(rucksack)//2])
    secondCompartment = set(rucksack[len(rucksack)//2:])

    return firstCompartment & secondCompartment



def lettersPriorityDeck():

    deck = {}
    for index, val in enumerate(ascii_letters):
        deck[val] = index + 1

    return deck
        

# Part 1
def RucksacksOrderScore(path):

    deck = lettersPriorityDeck()

    with open(path, "r") as rucksacks:

        orderScorePart1 = 0

        for rucksack in rucksacks.readlines():

            item = list(rucksackItem(rucksack))[0]

            orderScorePart1 += deck[item]
    
        return orderScorePart1 


# Part 2
def badgeGroupScore(path):

    deck = lettersPriorityDeck()

    with open(path, "r") as rucksacks:

        badgeScorePart2 = 0

        groups = rucksacks.readlines()
        for index in range(0, len(groups),3):

            groupe1 = set(groups[index].strip())
            groupe2 = set(groups[index + 1].strip())
            groupe3 = set(groups[index + 2].strip())
            
            intersection = groupe1 & groupe2 & groupe3

            item = list(intersection)[0]

            badgeScorePart2 += deck[item]

        return badgeScorePart2




print(badgeGroupScore("input.txt"))
