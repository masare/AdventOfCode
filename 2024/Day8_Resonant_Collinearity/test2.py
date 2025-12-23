import re
from math import sqrt


# function to get all antinode positions
def get_all_antinode_locs(rant, oant, endpoints):
    rstep = (rant[0] - oant[0])
    cstep = (rant[1] - oant[1])
    rpos = rant[0] + rstep
    cpos = rant[1] + cstep

    # add the current antenna position as an antinode
    antinode_locs = [rant]
    multiplier = 2
    while ((cpos > endpoints[0]) and (cpos < endpoints[1])) and ((rpos > endpoints[0]) and (rpos < endpoints[2])):
        antinode_locs.append((rpos, cpos)) # record current antinode position

        # compute new antinode position
        rpos = rant[0] + (rstep * multiplier)
        cpos = rant[1] + (cstep * multiplier)

        # update harmonic level
        multiplier += 1
    

    return antinode_locs

# function to compute the distance between two antennas
def compute_distance(ant1, ant2):
    return sqrt((ant1[0] - ant2[0])**2 + (ant1[1] - ant2[1])**2)

# function to generate antinodes
def gen_antinodes(antennas, endpoints):
    antinodes = [] # container to store all antinodes
    for freq, ants in antennas.items(): # iterate through all antennas for each frequency
        num_ants = len(ants) - 1 # get the number of antennas for the current frequency, excluding the last antenna
        for i in range(num_ants):
            rant = ants[i] # get the current antenna
            # iterate through all other antennas of the same frequency and check its relationship with them
            for oant in ants[i+1:]:
                dist = compute_distance(rant, oant) # get the distance between two antennas
                if dist > 1: # check if they are at least twice as far as each other
                    # get the all antinodes formed by antenna 1
                    antns1 = get_all_antinode_locs(rant, oant, endpoints)
                    # antns1.append(rant)
                    antinodes.extend(antns1)
                    # get the all antinodes formed by antenna 2
                    antns2 = get_all_antinode_locs(oant, rant, endpoints)
                    # antns2.append(oant)
                    antinodes.extend(antns2)
                    # antinodes.extend([antns1, antns2])
        
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
        
        for freq in freqs:
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
            

    print_map(ant_map)


# function to extract data from given path to file
def get_data(path):
    map = []
    with open(path, 'r') as file:
        for row in file.readlines():
            line = row.strip()
            
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
antinodes = gen_antinodes(antennas, endpoints)

# get valid antinodes
# val_antinodes = get_valid_antinodes(antinodes, endpoints)
val_antinodes = set(antinodes)

update_map_with_antinodes(val_antinodes, map)

# # print result statistics
print(f'Number of frequencies: {len(antennas.keys())}\nNumber of antennas: {len([ants for ants in antennas.values()])}')
print(f'Number of antinodes: {len(antinodes)}\nNumber of valid antinodes: {len(val_antinodes)}')
# # print(antinodes)
# print(antennas)
# print('---------')
# print(val_antinodes)
# print(endpoints)

