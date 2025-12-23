import numpy as np

# define a trail map node class
class MapNode:
    def __init__(self, node):
        self.node = node
        # self.value = value
        # self.trail_paths = get_trail_paths(node)

    def get_node_trail_paths(self):
        return get_trail_paths(self.node)
    
    

def get_node_value(node):
    return int(map[node[0]][node[1]])

# def is_a_trail()

def get_trail_paths(node):
    # print(type(node))
    directions = np.asarray([-1, 1, -1, 1], dtype=np.int8) # up, down, left, right
    paths = np.asarray([node[0], node[0], node[1], node[1]], dtype=np.int32) + directions
    bounds = get_map_boundaries(map)
    trail_paths = []
    # print(paths, bounds)
    # print(paths, bounds, get_node_value((paths[1], node[1])))
    # if paths[0] > bounds[0] and (get_node_value((paths[0], node[1])) - get_node_value(node) == 1): # check for upward movement
    #     trail_paths.append(MapNode((paths[0], node[1])))

    # if paths[1] < bounds[1] and (get_node_value((paths[1], node[1])) - get_node_value(node) == 1): # check for downward movement
    #     trail_paths.append(MapNode((paths[1], node[1])))

    # if paths[2] > bounds[2] and (get_node_value((node[0], paths[2])) - get_node_value(node) == 1): # check for left movement
    #     trail_paths.append(MapNode((node[0], paths[2])))

    # if directions[3] > bounds[3] and (get_node_value((node[0], paths[3])) - get_node_value(node) == 1): # check for right movement
    #     trail_paths.append(MapNode((node[0], paths[3])))

    if paths[0] > bounds[0] and (get_node_value((paths[0], node[1])) - get_node_value(node) == 1): # check for upward movement
        trail_paths.append((int(paths[0]), node[1]))

    if paths[1] < bounds[1] and (get_node_value((paths[1], node[1])) - get_node_value(node) == 1): # check for downward movement
        trail_paths.append((int(paths[1]), node[1]))

    if paths[2] > bounds[2] and (get_node_value((node[0], paths[2])) - get_node_value(node) == 1): # check for left movement
        trail_paths.append((node[0], int(paths[2])))

    if paths[3] < bounds[3] and (get_node_value((node[0], paths[3])) - get_node_value(node) == 1): # check for right movement
        trail_paths.append((node[0], int(paths[3])))

    # print(trail_paths)


    return trail_paths




# # define a trail class
# class Trail:
#     directions = np.asarray([-1, 1, -1, 1], dtype=np.int8) # up, down, left, right

#     def __init__(self, trailhead: tuple, map: list[str]):
#         self.trailhead = trailhead
#         # self.map = map
#         # self.trailheight = 0
#         self.trails = []
#         # self.current_pos = trailhead

#     # function to check if the next possible step is a valid trail step
#     def is_trailstep(self, current_pos, next_pos):
#         cstep = map[current_pos[0]][current_pos[1]]
#         nstep = map[next_pos[0]][next_pos[1]]

#         if nstep - cstep == 1: # check if current and next step difference is 1
#             return True
#         else:
#             return False 
#     # function to get next trail step
#     def get_pnext_step(self, current_pos):
#         pnext_step = []
#         directions = np.asarray([current_pos[0], current_pos[0], current_pos[1], current_pos[1]], dtype=np.int32) + Trail.directions
#         bounds = get_map_boundaries(map)

#         if directions[0] > bounds[0]: # check for upward movement
#             pnext_step.append((directions[0], current_pos[1]))

#         if directions[1] < bounds[1]: # check for downward movement
#             pnext_step.append((directions[1], current_pos[1]))

#         if directions[2] > bounds[2]: # check for left movement
#             pnext_step.append((current_pos[0], directions[2]))

#         if directions[3] > bounds[3]: # check for right movement
#             pnext_step.append((current_pos[0], directions[3]))

#     # function to begin trail search
#     def start_trail(self):

    
#     # function to get all trails
#     def get_trails(self):
#         ptrails = self.get_pnext_step()

    


#     def within_bounds(directions, map):
#         bounds = get_map_boundaries(map)
#         if directions[0] > bounds[0]


# extract trails of a trailhead
def get_trails(trailhead):
    # print(trailhead)
    trails = []
    ptrails = get_trail_paths(trailhead) # get immediate trail steps
    # ptrails = trailhead.get_node_trail_paths()
    # print(trailhead, ptrails)
    while True:
        trail_node = ptrails.pop()
        if (get_node_value(trail_node) == 9):# and (not trail_node in trails):
            trails.append(trail_node)
        else:
            ptrails.extend(get_trail_paths(trail_node))

        if len(ptrails) == 0:
            break

        # print(ptrails, trails, len(ptrails))

    return trails

# make trail
def make_trails(trailheads):
    trails = {}
    for trailhead in trailheads:
        # trails[trailhead] = get_trails(trailhead)
        trails[trailhead] = len(get_trails(trailhead))


    # def print_trails():
    #     for trailhead, trailends in trails.items():
    #         print(f'{trailhead}: {len(trailends)}')

    # print_trails()

    return trails
     

# # create a trail map
# def make_trail_map(map):
#     trail_map = {}
#     for i, path in enumerate(map):
#         for j, step in enumerate(path):
#             trail_map[MapNode((i,j))] = step

#     return trail_map

# function to get all trailheads (positions of 0's) in map
def get_trailheads(map: list[str]) -> list[tuple]:
    trailheads = []
    for i, path in enumerate(map): # iterate through all paths in map
        for j, pos in enumerate(path): # iterate through all positions in path
            if pos == '0': # check if position in path is a trailhead 
                trailheads.append((i, j)) # add a new trailhead

    return trailheads

# function to convert map to a list of lists
def map2list_of_lists(map: list[str]) -> list[list]:
    new_map = []
    for row in map:
        path = []
        for step in row:
            path.append(step)
        new_map.append(path)

    return new_map

# function to output map
def print_map(map):
    if type(map[0]) == str: # print map with path as a string
        print(*[path for path in map], sep='\n')
    else: # print map with path as a list
        for path in map:
            print(''.join(step for step in path))

# function to extract map boundary
def get_map_boundaries(map):
    return [-1, len(map), -1, len(map[0])] # up, down, left, right boundaries

# function to get map data
def get_map(path: str) -> list[str]:
    map = []
    with open(path, 'r') as file:
        for line in file.readlines():
            map.append(line.strip())

    return map

if __name__ == '__main__':
    # get map data
    # map = get_map('input_test') # get the map from test data
    map = get_map('input') # get the map from original puzzle data

    # view map
    # print(map)
    # print_map(map)
    # print_map(map2list_of_lists(map))
    
    # extract all trailheads
    trailheads = get_trailheads(map)

    # view trailheads
    # print(trailheads)

    # create trail map
    # trail_map = make_trail_map(map)

    # make trails
    trails = make_trails(trailheads)

    # print summary report
    print(f'Trailheads: {list(trails.keys())}')
    print(f'No. of Trails: {list(trails.values())}')
    print(f'Total Trails: {sum(trails.values())}')