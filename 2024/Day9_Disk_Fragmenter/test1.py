import re

def compute_checksum(sorted_file_space_sequences):
    checksum = 0

    for block in sorted_file_space_sequences:
        for id, data in enumerate(block):
            if data == '.':
                break
            checksum += (id * data)

    return checksum

# function to get the last file
def get_last_file(block):
    new_block = block.copy()
    new_block.reverse()
    for i, d in enumerate(new_block):
        if not d == '.':
            return -1-i

# function to sort sequences and group spaces in blocks
def sort_and_group_block_spaces(file_space_sequences):
    sorted_file_space_sequences = []

    for block in file_space_sequences:
        # print(block[0])
        sblock = ''.join(str(d) for d in block)
        # print(sblock)
        # print(re.findall(r'(?<=\.)[0-9]', sblock))
        # print(re.findall(r'(?>\.)[0-9]', sblock))
        while re.findall(r'(?<=\.)[0-9]', sblock):
            left_most_space = block.index('.')
            right_most_file = get_last_file(block)
            block[left_most_space] = block[right_most_file]
            block[right_most_file] = '.'
            sblock = ''.join(str(d) for d in block)
            # print(left_most_space, right_most_file, block[left_most_space], block[right_most_file],  block)
            # print(sblock)
            # break

        sorted_file_space_sequences.append(block)
    
    return sorted_file_space_sequences


# function to get file and space sequence of blocks
def get_file_space_sequence(data):
    fs_sequences = []
    for block in data:
        # print(block)
        lblock = [int(b) for b in block]
        files = lblock[0::2]
        spaces = lblock[1::2]

        # pad spaces to be of equal length as the number of files
        if len(files) > len(spaces):
            spaces.append(0)

        # sblock = ''
        sblock = []
        for id, fs in enumerate(zip(files, spaces)):
            # sblock += str(id)*fs[0] + '.'*fs[1]
            sblock.extend([id for i in range(fs[0])])
            sblock.extend(['.' for i in range(fs[1])])
            # print(id, fs, str(id)*fs[0] + '.'*fs[1])
        fs_sequences.append(sblock)
        # print(files, spaces)
    # print(fs_sequences)

    return fs_sequences

# function to get data
def get_data(path):
    data = []
    with open(path, 'r') as file:
        for line in file.readlines():
            # print(line)
            data.append(line.strip())

    return data

# get data
# data = get_data('input_test') # get test data
data = get_data('input') # get actual data

# view data
# print(data)

# get individaul representation of blocks in data
file_space_sequences = get_file_space_sequence(data)

# get spaces in individaul representation of blocks in data sorted
sorted_file_space_sequences = sort_and_group_block_spaces(file_space_sequences)

# compute checksum
checksum = compute_checksum(sorted_file_space_sequences)

# output final results
print(f'Checksum of data: {checksum}')

