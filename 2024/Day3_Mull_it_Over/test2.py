import re
import numpy as np

with open('input', 'r') as file:
    result = 0
    for line in file.readlines():
        # print(len(re.findall(r"do[(][)]", line)), len(line.split(r"do()")))
        # print(len(re.findall(r"don't()", line)), len(line.split(r"don't()")))
        # print(len(re.findall(r"do[(][)](.*don't[(][)])", line)))
        # print(line)
        # print('++++++++++++++++++++++'.join('-------------'.join(line.split(r"do()")).split(r"don't()")))
        # print('-------------'.join(line.split(r"do()")))
        # print(re.sub(r"do[(][)]", '+++++++++++++', line))
        d = line.split('do()')
        print(len(d))
        for i in d:
            print(i)
            j = re.sub("don't[(][)].*", '', i)
            print(j)
            # print(re.findall('mul[(](\d{1,3},\d{1,3})[)]', j))
            k = [m.split(',') for m in re.findall('mul[(](\d{1,3},\d{1,3})[)]', j)]
            print(k)
            l = np.asarray(k, dtype=np.int32)
            print(l)
            m = l[:,0] * l[:,1]
            print(m)
            result += m.sum()
            print(result, m.sum())
            
    # data = [line.split('do()') for line in file.readlines()]
    # data = [re.sub(r"don't[(][)].*", '', ''.join(d)) for d in data]
    # instructions = [re.findall('mul[(](\d{1,3},\d{1,3})[)]', d) for d in data]
    # print(data, len(data))
    # print(instructions)

    # instructions = [re.findall('mul[(](\d{1,3},\d{1,3})[)]', line) for line in file.readlines()]
    # # print(instructions[-1])
    # results = 0
    # for ins in instructions:
    #     l_ins = [i.split(',') for i in ins]
    #     np_ins = np.asarray(l_ins, dtype=np.int32)
    # #     # print(np_ins, np_ins.shape, np_ins[:,0]*np_ins[:, 1])
        
    #     results += (np_ins[:,0] * np_ins[:,1]).sum()
    # #     # print(ins, end='\n\n') 
    # #     # print(results, (np_ins[:,0] * np_ins[:,1]).sum())

    # print(results)