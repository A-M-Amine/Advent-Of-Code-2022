def subroutine(path):

    with open(path, "r") as dataStreamBuffer:

        line = dataStreamBuffer.read()

        start_of_packet_part1 = shortestSequencePosition(line,4)
        start_of_packet_part2 = shortestSequencePosition(line,14)

        print("part 1 ",start_of_packet_part1) 
        print("part 2 ",start_of_packet_part2) 
        


def shortestSequencePosition(line, length):

    i = length
    while len(set(line[i-length:i])) != length:
        i += 1
    
    return i


subroutine("input.txt")

