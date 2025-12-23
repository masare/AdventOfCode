import numpy as np
safe = 0
unsafe = 0


'''
Approach - Iteration 1
'''

def is_safe(levels, attempt=0):
    level_changes = [nxt_level - cur_level for cur_level, nxt_level  in zip(levels[:-1], levels[1:])]
    np_level_changes = np.asarray(level_changes, dtype=np.int16)

    if attempt > 1:
        return False

    no_change = (np_level_changes == 0).sum()
    if no_change > 0:
        if no_change == 1:
            # get index of repeating levels
            bad_level_index = np_level_changes.tolist().index(0)
            
            # make 2 copies of set of levels, each having one of the repeating levels removed
            levels_alt1 = levels[:]
            # levels_alt2 = levels[:]
            levels_alt1.pop(bad_level_index)
            # levels_alt2.pop(bad_level_index + 1)
            # print(levels_alt1, levels_alt2)
            
            # run the safe check on both to see if any of returns a true, then it is safe else unsafe
            # print(is_safe(levels=levels_alt1, attempt=attempt+1), is_safe(levels=levels_alt2, attempt=attempt+1))
            if not is_safe(levels=levels_alt1, attempt=attempt+1):
                return False
            # else:
            #     attempt += 1
        else:
            return False 
         
    etm_change = (abs(np_level_changes) > 3).sum()
    if etm_change > 0:
        if (etm_change == 1): #and (attempt == 0):
            # get index of extreme change levels
            bad_change = abs(np_level_changes).max()
            bad_level_index = 0
            if bad_change in np_level_changes:
                bad_level_index = np_level_changes.tolist().index(bad_change)
            else:
                bad_level_index = np_level_changes.tolist().index(-bad_change)
            
            # make 2 copies of set of levels, each having one of the levels contributing to the extreme change removed
            levels_alt1 = levels[:]
            levels_alt2 = levels[:]
            levels_alt1.pop(bad_level_index)
            levels_alt2.pop(bad_level_index + 1)
            # print(levels, levels_alt1, levels_alt2)
            
            # run the safe check on both to see if any of returns a true, then it is safe else unsafe
            # print(levels_alt1, is_safe(levels=levels_alt1, attempt=attempt+1))
            # print(levels_alt2, is_safe(levels=levels_alt2, attempt=attempt+1))
            if not((is_safe(levels=levels_alt1, attempt=attempt+1)) or (is_safe(levels=levels_alt2, attempt=attempt+1))):
                return False
            # else:
            #     # print(levels, levels_alt1, levels_alt2)
            #     attempt += 1
        else:
            return False
    
    cmplt_inc_change = (np_level_changes < 0).sum()
    cmplt_dec_change = (np_level_changes > 0).sum()
    if not ((cmplt_inc_change == 0) or (cmplt_dec_change == 0)):
        # if  attempt > 0:
        #     return False

        # print(levels, np_level_changes, cmplt_inc_change, cmplt_dec_change)
        if (cmplt_dec_change < cmplt_inc_change) and (cmplt_dec_change == 1):  # naturally decreasing with single errors
            # get index of abnormal levels
            bad_level_index = np_level_changes.tolist().index(np_level_changes.max())

            # make 2 copies of set of levels, each having one of the levels contributing to the abnormal change removed
            levels_alt1 = levels[:]
            levels_alt2 = levels[:]
            
            levels_alt1.pop(bad_level_index)
            levels_alt2.pop(bad_level_index + 1)
            # print(levels, levels_alt1, levels_alt2)

            # run the safe check on both to see if any of returns a true, then it is safe else unsafe
            # print(levels, levels_alt1, level_changes, is_safe(levels=levels_alt1, attempt=attempt+1))
            # print(levels, levels_alt2, level_changes, is_safe(levels=levels_alt2, attempt=attempt+1))
            if not((is_safe(levels=levels_alt1, attempt=attempt+1)) or (is_safe(levels=levels_alt2, attempt=attempt+1))):
                return False

        elif (cmplt_dec_change > cmplt_inc_change) and (cmplt_inc_change == 1):  # naturally increasing with single errors
            # get index of abnormal levels
            bad_level_index = np_level_changes.tolist().index(np_level_changes.min())

            # make 2 copies of set of levels, each having one of the levels contributing to the abnormal change removed
            levels_alt1 = levels[:]
            levels_alt2 = levels[:]
            
            levels_alt1.pop(bad_level_index)
            levels_alt2.pop(bad_level_index + 1)
            # print(levels, levels_alt1, levels_alt2)

            # run the safe check on both to see if any of returns a true, then it is safe else unsafe
            # print(levels, levels_alt1, level_changes, is_safe(levels=levels_alt1, attempt=attempt+1))
            # print(levels, levels_alt2, level_changes, is_safe(levels=levels_alt2, attempt=attempt+1))
            if not((is_safe(levels=levels_alt1, attempt=attempt+1)) or (is_safe(levels=levels_alt2, attempt=attempt+1))):
                return False
        else:
            return False

    # no_change = (np_level_changes == 0).sum()
    # if no_change > 0:
    #     print(levels, np_level_changes, attempt, cmplt_inc_change, cmplt_dec_change)
    #     if no_change > 1 or attempt > 1:
    #         print('______________________________')
    #         return False
    #     else:
    #         # get index of repeating levels
    #         bad_level_index = np_level_changes.tolist().index(0)
    #         print(levels[bad_level_index], levels[bad_level_index + 1])
    #         # make 2 copies of set of levels, each having one of the repeating levels removed
    #         levels_alt1 = levels[:]
    #         levels_alt2 = levels[:]
    #         levels_alt1.pop(bad_level_index)
    #         levels_alt2.pop(bad_level_index + 1)
    #         # run the safe check on both to see if any of returns a true, then it is safe else unsafe
    #         if not((is_safe(levels=levels_alt1, attempt=attempt+1)) or (is_safe(levels=levels_alt2, attempt=attempt+1))):
    #             return False 
    #         # pass 
         
    # etm_change = (abs(np_level_changes) > 3).sum()
    # if etm_change > 0:
    #     print(levels, np_level_changes, attempt, cmplt_inc_change, cmplt_dec_change)
    #     if etm_change > 1 or attempt > 1:
    #         print('-------------------------------')
    #         return False
    #     else:
    #         # get index of extreme change levels
    #         # print(levels, np_level_changes, attempt, abs(np_level_changes).max())
    #         bad_change = abs(np_level_changes).max()
    #         bad_level_index = 0
    #         if bad_change in np_level_changes:
    #             bad_level_index = np_level_changes.tolist().index(bad_change)
    #         else:
    #             bad_level_index = np_level_changes.tolist().index(-bad_change)
    #         print(levels[bad_level_index], levels[bad_level_index + 1])
    #         # make 2 copies of set of levels, each having one of the levels contributing to the extreme change removed
    #         levels_alt1 = levels[:]
    #         levels_alt2 = levels[:]
    #         levels_alt1.pop(bad_level_index)
    #         levels_alt2.pop(bad_level_index + 1)
    #         # run the safe check on both to see if any of returns a true, then it is safe else unsafe
    #         if not((is_safe(levels=levels_alt1, attempt=attempt+1)) or (is_safe(levels=levels_alt2, attempt=attempt+1))):
    #             return False
    #         # pass
    #         # return True
    
    # cmplt_inc_change = (np_level_changes < 0).sum()
    # cmplt_dec_change = (np_level_changes > 0).sum()
    # if not ((cmplt_inc_change == 0) or (cmplt_dec_change == 0)):
    #     print(levels, np_level_changes, attempt, cmplt_inc_change, cmplt_dec_change)
    #     if ((cmplt_dec_change < cmplt_inc_change) and (cmplt_dec_change > 1)) or (attempt > 1): # naturally decreasing but so many errors
    #         return False
    #     elif ((cmplt_inc_change < cmplt_dec_change) and (cmplt_inc_change > 1)) or (attempt > 1): # naturally increasing but so many errors
    #         return False
    #     elif (cmplt_dec_change < cmplt_inc_change) and (cmplt_dec_change == 1): # naturally decreasing with a single error
    #         # get index of abnormal change levels
    #         bad_level_index = np_level_changes.tolist().index(np_level_changes.max())
    #         print(levels[bad_level_index], levels[bad_level_index + 1])
    #         # make 2 copies of set of levels, each having one of the levels contributing to the abnormal change removed
    #         levels_alt1 = levels[:]
    #         levels_alt2 = levels[:]
    #         levels_alt1.pop(bad_level_index)
    #         levels_alt2.pop(bad_level_index + 1)
    #         # run the safe check on both to see if any of returns a true, then it is safe else unsafe
    #         if not((is_safe(levels=levels_alt1, attempt=attempt+1)) or (is_safe(levels=levels_alt2, attempt=attempt+1))):
    #             return False
    #         #pass
    #         # return True
    #     elif (cmplt_inc_change < cmplt_dec_change) and (cmplt_inc_change == 1): # naturally increasing with a single error
    #         # get index of abnormal change levels
    #         bad_level_index = np_level_changes.tolist().index(np_level_changes.min())
    #         print(levels[bad_level_index], levels[bad_level_index + 1])
    #         # make 2 copies of set of levels, each having one of the levels contributing to the abnormal change removed
    #         levels_alt1 = levels[:]
    #         levels_alt2 = levels[:]
    #         levels_alt1.pop(bad_level_index)
    #         levels_alt2.pop(bad_level_index + 1)
    #         # # run the safe check on both to see if any of returns a true, then it is safe else unsafe
    #         if not((is_safe(levels=levels_alt1, attempt=attempt+1)) or (is_safe(levels=levels_alt2, attempt=attempt+1))):
    #             return False
    #         # pass
    #         # return True

    return True




with open('input', 'r') as file:
    for line in file.readlines():
        levels = [int(level) for level in line.split()]
        
        if is_safe(levels):
            safe += 1
        else:
            unsafe += 1
        
        # print(f"Levels: {line}, Transitions: {level_changes}, Safe: {safe}, Unsafe: {unsafe}")
        # print(line, level_changes, unsafe)
        # print(levels)

print(f"Safe: {safe}, Unsafe: {unsafe}")
            
            
        