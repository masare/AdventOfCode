import numpy as np
safe = 0
unsafe = 0

# def is_unsafe(levels):
#     return (levels < 0).sum() > 0 and (levels > 0).sum() > 0
'''
Approach - Iteration 1
'''

# with open('input', 'r') as file:
#     for line in file.readlines():
#         levels = [int(level) for level in line.split()]
#         level_changes = []
#         for i, level in enumerate(levels[:-1]):
#             # if i < len(levels)-1:
#                 change = levels[i+1] - level
#                 level_changes.append(change)
#                 # l = len(level_changes)
#                 if change == 0 or abs(change) > 3:
#                     unsafe += 1
#                     # print('********************')
#                     break
#                 else:
#                     np_level_changes = np.asarray(level_changes, dtype=np.int16)
#                     # print((np_level_changes < 0).sum(), (np_level_changes > 0).sum(), l, (np_level_changes < 0).sum() > 0, (np_level_changes > 0).sum() > 0)
#                     if (np_level_changes < 0).sum() > 0 and (np_level_changes > 0).sum() > 0:
#                     # if is_unsafe(np_level_changes):
#                             unsafe += 1
#                             # print('++++++++++++++')
#                             break
#                     else:
#                         if i == len(levels)-2:
#                             safe += 1
#                             # print('------')

#         # if not is_unsafe(np_level_changes):
#         #      safe +=1
#         #      print('-----------------')
                
        
#         # print(f"Levels: {line}, Transitions: {level_changes}, Safe: {safe}, Unsafe: {unsafe}")
#         # print(line, level_changes, unsafe)

'''
Approach - Iteration 2
'''

with open('input', 'r') as file:
    for line in file.readlines():
        levels = [int(level) for level in line.split()]
        level_changes = [nxt_level - cur_level for cur_level, nxt_level  in zip(levels[:-1], levels[1:])]
        np_level_changes = np.asarray(level_changes, dtype=np.int16)
                
        no_change = (np_level_changes == 0).sum()
        etm_change = (abs(np_level_changes) > 3).sum()
        if (no_change > 0) or (etm_change > 0):
             unsafe += 1
             continue
        
        cmplt_inc_change = (np_level_changes < 0).sum()
        cmplt_dec_change = (np_level_changes > 0).sum()
        if (cmplt_inc_change == 0) or (cmplt_dec_change == 0):
             safe += 1
        else:
             unsafe += 1
        
        # print(f"Levels: {line}, Transitions: {level_changes}, Safe: {safe}, Unsafe: {unsafe}")
        # print(line, level_changes, unsafe)

print(f"Safe: {safe}, Unsafe: {unsafe}")
            
            
        