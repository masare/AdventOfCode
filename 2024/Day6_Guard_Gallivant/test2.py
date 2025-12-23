import numpy as np
import re

# data = np.genfromtxt('input', dtype='<U6')

# print(data)

path = [] # store the path of the guard

library = [] # stores the setting of the library environment

guard = () # stores the position of the guard

guard_direction = '' # keeps track of guard's current direction

guard_directions = ['^','>','v', '<'] # store all possible guard directions

out_pos = [] # stores library exit boundaries

obstacles = [] # stores positions of all obstacles

loopy_obstructions = [] # stores all possible positions where an obstacle can be placed to keep guard in a loop path

def set_loopy_obstruction():
    # check if the current path has an obstacle
    present, obstacle = check_obstacle_presence(direction=guard_direction, pos=guard)

    if not present: # if an obstacle is present
        # check_loopy_obstruction(next_pos=guard, obstacle=obstacle)
        # next_pos = guard # set current position
        # # get the next possible position to create obstruction in path
        # obstruction_pos = get_next_pos(direction=guard_direction, cur_pos=next_pos)

        # # get the next direction of guard if obstruction is created in path
        # next_direction = get_next_direction(cur_direction=guard_direction)


        # # iterate through all possible obstruction positions between the guards current position and the obstacle ahead
        # # while not (np.asarray(obstruction_pos) == np.asarray(obstacle)).all():
        # while not (obstruction_pos == obstacle):
        #     # check if there is an obstacle in the next direction after obstruction
        #     present, _ = check_obstacle_presence(direction=next_direction, pos=next_pos)
        #     # if an obstacle is present, add obstruction position to the list of possible obstructions
        #     if present:
        #         loopy_obstructions.append(obstruction_pos)
        #     # update current positon
        #     next_pos = obstruction_pos
        #     # get the next possible obstruction position
        #     obstruction_pos = get_next_pos(direction=guard_direction, cur_pos=next_pos)
            
            # pass
    # else:
        if guard_direction == '^':
            obstacle = (out_pos[0], guard[1])
        elif guard_direction == '>':
            obstacle = (guard[0], out_pos[1])
        elif guard_direction == 'v':
            obstacle = (out_pos[2], guard[1])
        else:
            obstacle = (guard[0], out_pos[3])

    check_loopy_obstruction(next_pos=guard, obstacle=obstacle)

def check_loopy_obstruction(next_pos, obstacle):
    # get the next possible position to create obstruction in path
    obstruction_pos = get_next_pos(direction=guard_direction, cur_pos=next_pos)

    # get the next direction of guard if obstruction is created in path
    next_direction = get_next_direction(cur_direction=guard_direction)


    # iterate through all possible obstruction positions between the guards current position and the obstacle ahead
    # while not (np.asarray(obstruction_pos) == np.asarray(obstacle)).all():
    while not (obstruction_pos == obstacle):
        # check if there is an obstacle in the next direction after obstruction
        present, _ = check_obstacle_presence(direction=next_direction, pos=next_pos)
        # if an obstacle is present, add obstruction position to the list of possible obstructions
        if present:
            loopy_obstructions.append(obstruction_pos)
        # update current positon
        next_pos = obstruction_pos
        # get the next possible obstruction position
        obstruction_pos = get_next_pos(direction=guard_direction, cur_pos=next_pos)

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



def mark_path():
    path.append(guard)
    # library[guard[0]][guard[1]] = 'X'
    # if path.count(guard) > 1:
    #     print('--------', guard, len(path))
    #     set_loopy_obstruction()

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
    
def get_next_pos(direction, cur_pos):
    if direction == '^':
        return (cur_pos[0]-1, cur_pos[1])
    elif direction == '>':
        return (cur_pos[0], cur_pos[1]+1)
    elif direction == 'v':
        return (cur_pos[0]+1, cur_pos[1])
    else:
        return (cur_pos[0], cur_pos[1]-1)

def update_library(next_pos):
    global guard

    library[guard[0]][guard[1]] = '.'
    library[next_pos[0]][next_pos[1]] = guard_direction
    guard = next_pos

def print_library():
    for row in library:
        print(''.join(i for i in row))
    print('\n\n')

def get_next_direction(cur_direction):
    gdi = guard_directions.index(cur_direction)
    if gdi == 3:
        return guard_directions[0]
    else:
        return guard_directions[gdi+1]

def make_path():
    global guard_direction, guard_directions
    while True:
        mark_path()
        next_pos = get_next_pos(direction=guard_direction, cur_pos=guard)
        
        # if ((next_pos[0] >= 0) and (next_pos[0] < len(library))) and ((next_pos[1] >= 0) and (next_pos[1] < len(library[0]))):
        if check_out(next_pos=next_pos):
            print(out_pos, next_pos)
            break

        if library[next_pos[0]][next_pos[1]] == '#':
            # gdi = guard_directions.index(guard_direction)
            # if gdi == 3:
            #     guard_direction = guard_directions[0]
            # else:
            #     guard_direction = guard_directions[gdi+1]
            guard_direction = get_next_direction(cur_direction=guard_direction)
            next_pos = get_next_pos(direction=guard_direction, cur_pos=guard)
        
        update_library(next_pos=next_pos)
        # print_library()

def get_all_obstacles(index, row):
    for i, step in enumerate(row):
        if step == '#':
            obstacles.append((index, i))


# get environment setting
# with open('input', 'r') as file:
with open('input_test', 'r') as file:
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

    make_path()

    print(f'Initial Guard Position: {guard} \nInitial Guard Direction: {guard_direction}')
    print(f'Total Moves: {len(path)} \nTotal Distinct Positions: {len(set(path))}')
    print(f'Possible Obstructions: {len(loopy_obstructions)} \nObstructions: {loopy_obstructions}')
