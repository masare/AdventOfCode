import re
import numpy as np

def get_dos(data):
    # print(re.findall("(?s)(?<=do[(][)]).*?(?=don't[(][)])", data))
    # d = data.split('do()')
    # line = ''
    # for i in d:
    #     line = ''.join(re.sub("don't[(][)].*", '', i))

    # return line
    # p1 = re.findall("(?s).*?(?=do[(][)]|don't[(][)])", data)[0]
    # print(re.findall("(?s).*?(?=do[(][)]|don't[(][)])", data)[0])
    # print(re.findall("(?s)(?<=do[(][)]).*?(?=don't[(][)]|$)", data))
    return ''.join(d for d in re.findall("(?s)(?<=do[(][)]).*?(?=don't[(][)]|$)", data))

def get_donts(data):
    # d = data.split('do()')
    # line = ''
    # for i in d:
    #     line = ''.join(k for k in re.findall("don't[(][)].*", i))
    #     # print(j)
    #     # print(len(re.split("don't[(][)]", j)), end='\n\n')

    # return line
    # print(re.findall("(?s)(?<=don't[(][)]).*?(?=do[(][)]){0,1}", data))
    return ''.join(d for d in re.findall("(?s)(?<=don't[(][)]).*?(?=do[(][)]|$)", data))

def compt_mul(data):
    instructions = re.findall('mul[(]([0-9]{1,3},[0-9]{1,3})[)]', data)
    # print(instructions)
    # print(instructions[-1])
    
    l_ins = []
    # for ins in instructions:
        # l_ins.append(ins.split(','))
    l_ins.extend(ins.split(',') for ins in instructions)
    # print(l_ins)
    np_ins = np.asarray(l_ins, dtype=np.int32)
    # print(np_ins, np_ins.shape, np_ins[:,0]*np_ins[:, 1])

    return (np_ins[:,0] * np_ins[:,1]).sum() 


with open('input', 'r') as file:
    result = 0
    # dos = ''
    # donts = ''
    data = ''
    for line in file.readlines():
        # print(len(re.findall(r"do[(][)]", line)), len(line.split(r"do()")))
        # print(len(re.findall(r"don't()", line)), len(line.split(r"don't()")))
        # print(len(re.findall(r"do[(][)](.*don't[(][)])", line)))
        # print(line)
        # print('++++++++++++++++++++++'.join('-------------'.join(line.split(r"do()")).split(r"don't()")))
        # print('-------------'.join(line.split(r"do()")))
        # print(re.sub(r"do[(][)]", '+++++++++++++', line))
        data += line
        # dos += get_dos(line)
        # donts += get_donts(line)
        # print(data, dos, donts, sep='\t\t', end='\n\n')
    # dos = get_dos(data)
    donts = get_donts(data)
    # print(compt_mul(dos))
    # print(compt_mul(donts))
    # print(compt_mul(data))
    print(compt_mul(data) - compt_mul(donts))
        # d = line.split('do()')
        # print(len(d))
        # for i in d:
        #     print(i)
        #     j = re.sub("don't[(][)].*", '', i)
        #     print(j)
        #     # print(re.findall('mul[(](\d{1,3},\d{1,3})[)]', j))
        #     k = [m.split(',') for m in re.findall('mul[(](\d{1,3},\d{1,3})[)]', j)]
        #     print(k)
        #     l = np.asarray(k, dtype=np.int32)
        #     print(l)
        #     m = l[:,0] * l[:,1]
        #     print(m)
        #     result += m.sum()
        #     print(result, m.sum())
            
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