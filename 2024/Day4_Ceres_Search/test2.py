import numpy as np

# create filters
bfilter = [['M','.','S'],['.','A','.'],['M','.','S']]

filters = []

flt = np.asarray(bfilter)
filters.append(flt)
flt = flt.T # transpose the basic filter and add it as another filter
filters.append(flt)
bfilter = flt.tolist()
bfilter.reverse()
flt = np.asarray(bfilter)
filters.append(flt)
flt = flt.T # transpose the basic filter and add it as another filter
filters.append(flt) 

# print(filters)

# get data
data = []
with open('input', 'r') as file:
    for line in file.readlines():
        line = line.strip()
        data.append(list(line))
    
    data = np.asarray(data)

# print(data)

# search for matches
matches = 0
dr, dc = data.shape # extract number of rows and columns in data
fr, fc = flt.shape # extract number of rows and columns in filter (all filters have same shape)

# compute total number of rows and columns to be traversed
rows = dr-fr+1
cols = dc-fc+1

for flt in filters:
    for i in range(rows):
        for j in range(cols):
            xmatch = data[i:i+fr, j:j+fc] == flt
            if xmatch.sum() == 5:
                matches += 1

print(matches)