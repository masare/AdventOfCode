import numpy as np

# Approach - Iteration 1
'''
Using both numpy and open
'''
# data = []
# with open("input", 'r') as file:
#     for line in file.readlines():
#         # print(line)
#         data.append(line.split())

# # convert the distance data to numpy array for easy manipulation
# data = np.asarray(data, dtype=np.int32)

# # Sort the two sets of distances separately
# data[:,0] = np.sort(data[:,0])
# data[:,1] = np.sort(data[:,1])

# # Compute overall sum of difference in the distances
# total_distance = np.abs(np.diff(data, axis=1)).sum()

# # Output final results
# print(total_distance)


# Approach - Iteration 2
'''
Using purely numpy
'''
# load the data
data = np.genfromtxt('input', dtype=np.int32)

# sort individual columns
data[:,0] = np.sort(data[:,0])
data[:,1] = np.sort(data[:,1])

# compute the difference in distances
data_diff = np.abs(np.diff(data, axis=1))

# compute the overall total distance
sum_data_diff = data_diff.sum()
# compute and output the sum total of the difference in column values
# print(np.abs(np.diff(data, axis=1)).sum())
print(sum_data_diff)
