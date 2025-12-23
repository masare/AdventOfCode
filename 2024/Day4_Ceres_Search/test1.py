import numpy as np

# Create filters
bfilters = [['X','M','A','S'],['S','A','M','X'],[['X','.','.','.'], ['.','M','.','.'], ['.','.','A','.'], ['.','.','.','S']],
           [['.','.','.','X'], ['.','.','M','.'], ['.','A','.','.'], ['S','.','.','.']]]

filters = []

for ind, bflt in enumerate(bfilters):
    if ind < 2:
        flt = np.asarray(bflt).reshape((1,4))
        filters.append(flt)
        filters.append(flt.reshape((4,1)))
    else:
        flt = np.asarray(bflt)
        filters.append(flt)
        bflt.reverse()
        flt = np.asarray(bflt)
        filters.append(flt)

# print(filters)

# Get data
data = []
with open('input', 'r') as file:
    for line in file.readlines():
        line = line.strip()
        data.append(list(line))

    data = np.asarray(data)

# print(data)

# Search for XMAS patterns
matches = 0
dr, dc = data.shape # get the shape of data
for flt in filters:
    fr, fc = flt.shape # get the shape of filter
    for i in range(dr-fr+1):
        for j in range(dc-fc+1):
            xmatch = data[i:i+fr, j:j+fc] == flt
            if xmatch.sum() == 4:
                matches += 1

print(matches)