

def paircheck(path):

    with open(path, "r") as assignments:

        pairsCountPart1 = 0
        pairsCountPart2 = 0

        for pairs in assignments.readlines():

            pair1, pair2 = pairs.split(",")

            p1 = [int(i) for i in pair1.split("-")]
            p2 = [int(i) for i in pair2.split("-")]
            
            # generate sets of assignmets
            lst1 = {i for i in range(p1[0],p1[1] + 1)}
            lst2 = {i for i in range(p2[0],p2[1] + 1)}

            # check for intersections
            inter = lst1 & lst2

            if inter == lst1 or inter == lst2:
                pairsCountPart1 += 1

            if len(inter) > 0:
                pairsCountPart2 += 1

        print(pairsCountPart1)
        print(pairsCountPart2)


paircheck("input.txt")