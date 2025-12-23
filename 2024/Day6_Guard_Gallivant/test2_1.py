import numpy as np
import re

# data = np.genfromtxt('input', dtype='<U6')

# print(data)

path = [] # store the path of the guard

loopy_path = [] # store path of the guard's position and direction

# library = [] # stores the setting of the library environment

# guard = () # stores the position of the guard

# guard_direction = '' # keeps track of guard's current direction

guard_directions = ['^','>','v', '<'] # store all possible guard directions

# out_pos = [] # stores library exit boundaries

obstacles = [] # stores positions of all obstacles

loopy_obstructions = [] # stores all possible positions where an obstacle can be placed to keep guard in a loop path

def get_possible_obstructions():
    obstructions = []
    # print(path)
    # extract all positions not in guard's starting direction or position as possible positions for obstruction
    for step in path:
        # print(step, guard)
        # if (guard_direction == '^') and not (step[1] == guard[1] and step[0] <= guard[0]):
        #     # print('^^^^^^^^^^^^^^^')
        #     obstructions.append(step)
        # elif (guard_direction == '>') and not (step[0] == guard[0] and step[1] >= guard[1]):
        #     # print('>>>>>>>>>>>>>>>')
        #     obstructions.append(step)
        # elif (guard_direction == 'v') and not (step[1] == guard[1] and step[0] >= guard[0]):
        #     # print('vvvvvvvvvvvvvvv')
        #     obstructions.append(step)
        # elif (guard_direction == '<') and not (step[0] == guard[0] and step[1] <= guard[1]):
        #     # print('<<<<<<<<<<<<<<<')
        #     obstructions.append(step)

        # given that only the guard's starting position cannot have an obstacle
        if not step == guard:
            obstructions.append(step)
    
    return obstructions

def set_loopy_obstruction():
    obstructions_pos = get_possible_obstructions() 
    # print(obstructions_pos)

    for obstacle_pos in obstructions_pos:
        global loopy_path
        library, _, __, ___ = get_library_data()
        cur_library = add_obstruction(obstacle_pos=obstacle_pos, cur_library=library)
        # print(obstacle_pos)
        # print_library(cur_library)
        # print_library(library)
        # break
        # print('-----------------', obstacle_pos)
        loopy_path = []
        loopy, cur_pos, cur_direction = make_loopy_path(cur_library=cur_library)
        if loopy:
            # print('#################', obstacle_pos)
            # check if there is an obstacle in the direction after obstruction
            present, _ = check_obstacle_presence(direction=cur_direction, pos=cur_pos)
            # if an obstacle is present, add obstruction position to the list of possible obstructions
            if present:
                # print('++++++++++++++', cur_pos, cur_direction)
                loopy_obstructions.append(obstacle_pos)

    # # check if the current path has an obstacle
    # present, obstacle = check_obstacle_presence(direction=guard_direction, pos=guard)

    # if not present: # if an obstacle is present
    #     # check_loopy_obstruction(next_pos=guard, obstacle=obstacle)
    #     # next_pos = guard # set current position
    #     # # get the next possible position to create obstruction in path
    #     # obstruction_pos = get_next_pos(direction=guard_direction, cur_pos=next_pos)

    #     # # get the next direction of guard if obstruction is created in path
    #     # next_direction = get_next_direction(cur_direction=guard_direction)


    #     # # iterate through all possible obstruction positions between the guards current position and the obstacle ahead
    #     # # while not (np.asarray(obstruction_pos) == np.asarray(obstacle)).all():
    #     # while not (obstruction_pos == obstacle):
    #     #     # check if there is an obstacle in the next direction after obstruction
    #     #     present, _ = check_obstacle_presence(direction=next_direction, pos=next_pos)
    #     #     # if an obstacle is present, add obstruction position to the list of possible obstructions
    #     #     if present:
    #     #         loopy_obstructions.append(obstruction_pos)
    #     #     # update current positon
    #     #     next_pos = obstruction_pos
    #     #     # get the next possible obstruction position
    #     #     obstruction_pos = get_next_pos(direction=guard_direction, cur_pos=next_pos)
            
    #         # pass
    # # else:
    #     if guard_direction == '^':
    #         obstacle = (out_pos[0], guard[1])
    #     elif guard_direction == '>':
    #         obstacle = (guard[0], out_pos[1])
    #     elif guard_direction == 'v':
    #         obstacle = (out_pos[2], guard[1])
    #     else:
    #         obstacle = (guard[0], out_pos[3])

    # check_loopy_obstruction(next_pos=guard, obstacle=obstacle)

# def check_loopy_obstruction(next_pos, obstacle):
#     # get the next possible position to create obstruction in path
#     obstruction_pos = get_next_pos(direction=guard_direction, cur_pos=next_pos)

#     # get the next direction of guard if obstruction is created in path
#     next_direction = get_next_direction(cur_direction=guard_direction)


#     # iterate through all possible obstruction positions between the guards current position and the obstacle ahead
#     # while not (np.asarray(obstruction_pos) == np.asarray(obstacle)).all():
#     while not (obstruction_pos == obstacle):
#         # check if there is an obstacle in the next direction after obstruction
#         present, _ = check_obstacle_presence(direction=next_direction, pos=next_pos)
#         # if an obstacle is present, add obstruction position to the list of possible obstructions
#         if present:
#             loopy_obstructions.append(obstruction_pos)
#         # update current positon
#         next_pos = obstruction_pos
#         # get the next possible obstruction position
#         obstruction_pos = get_next_pos(direction=guard_direction, cur_pos=next_pos)

def check_obstacle_presence(direction, pos):
    for obstacle in obstacles:
        if (direction == '^') and (obstacle[0] < pos[0]) and (obstacle[1] == pos[1]):
            return True, obstacle
        elif (direction == 'v') and (obstacle[0] > pos[0]) and (obstacle[1] == pos[1]):
            return True, obstacle
        elif (direction == '>') and (obstacle[1] > pos[1]) and (obstacle[0] == pos[0]):
            return True, obstacle
        elif (direction == '<') and (obstacle[1] < pos[1]) and (obstacle[0] == pos[0]):
            return True, obstacle
    
    if direction == '^':
        return False, (out_pos[0], pos[1])
    elif direction == '>':
        return False, (pos[1], out_pos[1])
    elif direction == 'v':
        return False, (out_pos[2], pos[1])
    else:
        return False, (pos[0], out_pos[3])
    # return False

loopy = False

def mark_loopy_path(cur_pos, cur_direction):
    step = (cur_pos, cur_direction)
    # library[guard[0]][guard[1]] = 'X'
    if step in loopy_path:
        # print('-------------------')
        # print(step, loopy_path)
        return True
    else:
        loopy_path.append(step)
        # path.append(cur_pos)
        return False
    

def mark_path(cur_pos):
    path.append(cur_pos)
    # #     print('--------', guard, len(path))
    # #     set_loopy_obstruction()

def check_out(next_pos, cur_direction):
    if (cur_direction == '^') and (next_pos[0] == out_pos[0]):
        return True
    elif (cur_direction == '>') and (next_pos[1] == out_pos[1]):
        return True
    elif (cur_direction == 'v') and (next_pos[0] == out_pos[2]):
        return True
    elif (cur_direction == '<') and (next_pos[1] == out_pos[3]):
        return True
    else:
        return False
    
def get_next_pos(direction, cur_pos):
    if direction == '^':
        return (cur_pos[0]-1, cur_pos[1])
    elif direction == '>':
        return (cur_pos[0], cur_pos[1]+1)
    elif direction == 'v':
        return (cur_pos[0]+1, cur_pos[1])
    else:
        return (cur_pos[0], cur_pos[1]-1)

def update_library(cur_pos, next_pos, cur_direction, cur_library):
    cur_library[cur_pos[0]][cur_pos[1]] = '.'
    cur_library[next_pos[0]][next_pos[1]] = cur_direction
    
    return next_pos, cur_library

def add_obstruction(obstacle_pos, cur_library):
    
    cur_library[obstacle_pos[0]][obstacle_pos[1]] = '#'
    
    return cur_library

def print_library(cur_library):
    for row in cur_library:
        print(''.join(i for i in row))
    print('\n\n')

def get_next_direction(cur_direction):
    gdi = guard_directions.index(cur_direction)
    if gdi == 3:
        return guard_directions[0]
    else:
        return guard_directions[gdi+1]

def make_path(cur_library):
    # global guard_directions
    cur_pos = guard
    cur_direction = guard_direction
    while True:
        mark_path(cur_pos=cur_pos)
        next_pos = get_next_pos(direction=cur_direction, cur_pos=cur_pos)
        
        # if ((next_pos[0] >= 0) and (next_pos[0] < len(library))) and ((next_pos[1] >= 0) and (next_pos[1] < len(library[0]))):
        if check_out(next_pos=next_pos, cur_direction=cur_direction):
            # print(out_pos, next_pos)
            break

        if cur_library[next_pos[0]][next_pos[1]] == '#':
            # gdi = guard_directions.index(guard_direction)
            # if gdi == 3:
            #     guard_direction = guard_directions[0]
            # else:
            #     guard_direction = guard_directions[gdi+1]
            cur_direction = get_next_direction(cur_direction=cur_direction)
            next_pos = get_next_pos(direction=cur_direction, cur_pos=cur_pos)
        
        cur_pos, cur_library = update_library(cur_pos=cur_pos, next_pos=next_pos, cur_direction=cur_direction, cur_library=cur_library)
        # print_library(cur_library)
    # print_library(cur_library)
    # print_library(library)

def make_loopy_path(cur_library):
    # global guard_directions
    cur_pos = guard
    cur_direction = guard_direction
    while True:
        loopy = mark_loopy_path(cur_pos=cur_pos, cur_direction=cur_direction)
        if loopy:
            return True, cur_pos, cur_direction
        
        next_pos = get_next_pos(direction=cur_direction, cur_pos=cur_pos)
        
        if check_out(next_pos=next_pos, cur_direction=cur_direction):
            # print(out_pos, next_pos, cur_pos)
            break
        # else:
        #     print(next_pos)

        while cur_library[next_pos[0]][next_pos[1]] == '#':
            
            cur_direction = get_next_direction(cur_direction=cur_direction)
            next_pos = get_next_pos(direction=cur_direction, cur_pos=cur_pos)
            # print(next_pos, cur_direction)
        cur_pos, cur_library = update_library(cur_pos=cur_pos, next_pos=next_pos, cur_direction=cur_direction, cur_library=cur_library)
        # print_library(cur_library)
    return False, cur_pos, cur_direction

def get_all_obstacles(index, row):
    for i, step in enumerate(row):
        if step == '#':
            obstacles.append((index, i))

def get_library_copy(library):
    library_copy = []
    for row in library:
        library_copy.append()
    return [row for row in library]

def get_library_data():
    guard_direction = ''
    guard = ()
    library = []
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
            get_all_obstacles(index=i, row=p)

        out_pos = [-1, len(library[0]), len(library), -1]
    
    return library, guard, guard_direction, out_pos
    # ll = library[:]
    # print_library(ll)
library, guard, guard_direction, out_pos = get_library_data()
# cur_library, _, __, ___ = get_library_data()
make_path(cur_library=library) # extract path of guard without additional obstruction
# print_library(ll)
set_loopy_obstruction() # locate all possible loopy obstructions in guard's path
# cur_library = [row for row in library]
# cur_library = add_obstruction(obstacle_pos=(7,7), cur_library=cur_library)
# make_loopy_path(cur_library=library)
# print_library(library)
# print(library)
# print(cur_library)

print(f'Initial Guard Position: {guard} \nInitial Guard Direction: {guard_direction}')
print(f'Total Moves: {len(path)} \nTotal Distinct Positions: {len(set(path))}')
print(f'Possible Obstructions: {len(loopy_obstructions)} \nObstructions: {len(set(loopy_obstructions))}')
