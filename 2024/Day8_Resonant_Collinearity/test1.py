import re
from math import sqrt

# functio to extract proper antinode locations
def get_valid_antinodes(antinodes, endpoints):
    val_antinodes = []
    for antn in set(antinodes):
        if ((antn[0] > endpoints[0]) and (antn[0] < endpoints[1])) and ((antn[1] > endpoints[0]) and (antn[1] < endpoints[2])):
            val_antinodes.append(antn)

    return val_antinodes

# function to get antinode position
def get_antinode_loc(rant, oant):
    rpos = rant[0] + (rant[0] - oant[0])
    cpos = rant[1] + (rant[1] - oant[1])
    return rpos, cpos 

# function to compute the distance between two antennas
def compute_distance(ant1, ant2):
    return sqrt((ant1[0] - ant2[0])**2 + (ant1[1] - ant2[1])**2)

# function to generate antinodes
def gen_antinodes(antennas):
    antinodes = [] # container to store all antinodes
    for freq, ants in antennas.items(): # iterate through all antennas for each frequency
        num_ants = len(ants) - 1 # get the number of antennas for the current frequency, excluding the last antenna
        for i in range(num_ants):
            rant = ants[i] # get the current antenna
            # iterate through all other antennas of the same frequency and check its relationship with them
            for oant in ants[i+1:]:
                dist = compute_distance(rant, oant) # get the distance between two antennas
                if dist > 1: # check if they are at least twice as far as each other
                    # get the two antinodes formed
                    antn1 = get_antinode_loc(rant, oant)
                    antn2 = get_antinode_loc(oant, rant)

                    antinodes.extend([antn1, antn2])
        
        # if freq == '3':
        #     # print(antinodes)
        #     break
    return antinodes        


# function to extract antennae positions categorised by their frequencies
def get_antennas(map):
    antennas ={}
    for i, row in enumerate(map):
        # freqs = re.findall(r'(?<=\.)[0-9a-zA-Z]{1}\.', row)
        freqs = re.findall(r'[0-9a-zA-Z]{1}', row)
        # print(re.findall(r'(?<=\.)[0-9a-zA-Z]{1}\.', row))
        # for j, freq in enumerate(row):
        for freq in freqs:
        #     if not re.findall(r'[0-9a-zA-Z]', freq) == []:
        #         # print(i, j, data)
                j = row.index(freq[0])
                if freq[0] in antennas.keys():
                    antennas[freq[0]]. append((i, j))
                else:
                    antennas[freq[0]] = [(i,j)]
        # print(antennas)
    
    return antennas

# function to print data in map
def print_map(map):
    for row in map:
        print(''.join(d for d in row))
        # print(row)

def update_map_with_antinodes(antinodes, map):
    ant_map = map.copy()

    def string2llist(s):
        l = []
        for d in s:
            l.append(d)
        return l
    
    for ant in antinodes:
        # print(ant)
        data = ant_map[ant[0]]
        if data[ant[1]] == '.':
            dl = string2llist(data)
            dl[ant[1]] = '#'
            ant_map[ant[0]] = ''.join(d for d in dl)
            # print(dl, data)
        
        # ant_map.append(data)
            
    # for i, row in enumerate(map):
    #     data = ''
    #     for j, d in enumerate(row):
    #         # if (i, j) in antinodes:
    #         #     print('___________')
    #         # if d == '.':
    #         #     print('+++++++++++')
    #         if ((i, j) in antinodes) and (d == '.'):
    #             # data.append('#')
    #             data = row[:j] + '#' + row[j+1:]
    #         # else:
    #             # data.append(d)
    #             # data = row[:]
    #     ant_map.append(data)

    print_map(ant_map)


# function to extract data from given path to file
def get_data(path):
    map = []
    with open(path, 'r') as file:
        for row in file.readlines():
            line = row.strip()
            # data = []
            # for d in line:
            #     data.append(d)
            # map.append(data)
            map.append(line)

    endpoints = [-1, len(map[0]), len(map)]

    return map, endpoints

# get data
# map, endpoints = get_data('input_test') # test input data
map, endpoints = get_data('input') # input data

# print data
# print_map(map)

# get antennas
antennas = get_antennas(map)

# view all antennas
# print(antennas)

# generate antinodes
antinodes = gen_antinodes(antennas)

# get valid antinodes
val_antinodes = get_valid_antinodes(antinodes, endpoints)

update_map_with_antinodes(val_antinodes, map)

# # print result statistics
print(f'Number of frequencies: {len(antennas.keys())}\nNumber of antennas: {len([ants for ants in antennas.values()])}')
print(f'Number of antinodes: {len(antinodes)}\nNumber of valid antinodes: {len(val_antinodes)}')
# # print(antinodes)
# print(antennas)
# print('---------')
# print(val_antinodes)
# print(endpoints)

