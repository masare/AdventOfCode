import re
import numpy as np

with open('input', 'r') as file:
    instructions = [re.findall('mul[(](\d{1,3},\d{1,3})[)]', line) for line in file.readlines()]
    # print(instructions[-1])
    results = 0
    for ins in instructions:
        l_ins = []
        for i in ins:
            l_ins.append(i.split(','))
        np_ins = np.asarray(l_ins, dtype=np.int32)
        # print(np_ins, np_ins.shape, np_ins[:,0]*np_ins[:, 1])

        results += (np_ins[:,0] * np_ins[:,1]).sum()
        # print(ins, end='\n\n') 
        # print(results, (np_ins[:,0] * np_ins[:,1]).sum())

    print(results)
    # for line in file.readlines():

        # print(re.findall('mul[(](\d{1,3},\d{1,3})[)]', line))