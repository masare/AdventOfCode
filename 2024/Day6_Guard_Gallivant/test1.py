import numpy as np
import re

# data = np.genfromtxt('input', dtype='<U6')

# print(data)

path = [] # store the path of the guard

library = [] # stores the setting of the library environment

guard = () # stores the position of the guard

guard_direction = ''

guard_directions = ['^','>','v', '<']

out_pos = []

def mark_path():
    path.append(guard)
    # library[guard[0]][guard[1]] = 'X'

def check_out(next_pos):
    if (guard_direction == '^') and (next_pos[0] == out_pos[0]):
        return True
    elif (guard_direction == '>') and (next_pos[1] == out_pos[1]):
        return True
    elif (guard_direction == 'v') and (next_pos[0] == out_pos[2]):
        return True
    elif (guard_direction == '<') and (next_pos[1] == out_pos[3]):
        return True
    else:
        return False
    
def get_next_pos():
    if guard_direction == '^':
        return (guard[0]-1, guard[1])
    elif guard_direction == '>':
        return (guard[0], guard[1]+1)
    elif guard_direction == 'v':
        return (guard[0]+1, guard[1])
    else:
        return (guard[0], guard[1]-1)

def update_library(next_pos):
    global guard

    library[guard[0]][guard[1]] = '.'
    library[next_pos[0]][next_pos[1]] = guard_direction
    guard = next_pos

def print_library():
    for row in library:
        print(''.join(i for i in row))
    print('\n\n')

def make_path():
    global guard_direction, guard_directions
    while True:
        mark_path()
        next_pos = get_next_pos()
        
        # if ((next_pos[0] >= 0) and (next_pos[0] < len(library))) and ((next_pos[1] >= 0) and (next_pos[1] < len(library[0]))):
        if check_out(next_pos=next_pos):
            print(out_pos, next_pos)
            break

        if library[next_pos[0]][next_pos[1]] == '#':
            gdi = guard_directions.index(guard_direction)
            if gdi == 3:
                guard_direction = guard_directions[0]
            else:
                guard_direction = guard_directions[gdi+1]
            next_pos = get_next_pos()
        
        update_library(next_pos=next_pos)
        # print_library()


# get environment setting
with open('input', 'r') as file:
# with open('input_test', 'r') as file:
    for i, line in enumerate(file.readlines()):
        p = list(line.strip())
        library.append(p)
        if guard_direction == '':
            for gd in guard_directions:
                if gd in line:
                    guard = (i, line.index(gd))
                    guard_direction = gd
                    break

    out_pos = [-1, len(library[0]), len(library), -1]

    make_path()

    print(f'Initial Guard Position: {guard} \nInitial Guard Direction: {guard_direction}')
    print(f'Total Moves: {len(path)} \nTotal Distinct Positions: {len(set(path))}')
