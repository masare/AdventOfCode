import re

def compute_checksum(sorted_file_space_sequences):
    checksum = 0

    for block in sorted_file_space_sequences:
        for id, data in enumerate(block):
            if data == '.':
                continue
            checksum += (id * data)

    return checksum

# function to get files in decreasing order
def get_files_decreasing_order(block):
    new_block = block.copy()
    new_block.reverse()
    files = {}
    for d in new_block:
        # files[d] = ds
        # if (not d == '.') and (not d in files):
        #     ds = new_block.count(d)
        #     files[d] = ds
        if (d == '.') or (d in files):
            continue
        ds = new_block.count(d)
        files[d] = ds

    return files

# function to get the next highest order file
def get_next_highest_order_file(block, files):
    new_block = block.copy()
    new_block.reverse()
    for d in new_block:
        if (d == '.') or (d in files):
            continue
        else:
            files[d] = new_block.count(d)
            return d, files
    
    return '', files

        

# function to check if file has a befitting space
def has_befitting_space(fs, spaces):
    for space in spaces:
        if fs <= len(space):
            return True
        
    return False

# function to get indices corresponding to befitting space
def get_space_indices(file, fs, block):
    # print(fs)
    space_indices = []
    sblock = ''
    fi = block.index(file) # index of file
    for i, d in enumerate(block):
        if i >= fi:
            break
        sblock += str(d)
        pattern = '(?>[.]{' + str(fs) + '})'
        # print(fs, pattern)
        if re.findall(pattern, sblock):
            # print(sblock)
            space_indices = [i-j for j in range(fs)]
            break
    
    return space_indices

# function to get indices corresponding to file
def get_file_indices(file, block):
    if file in block:
        fi = block.index(file)
        fs = block.count(file)
        return [fi+i for i in range(fs)]
    else:
        return []
    # file_indices = []
    # sblock = ''
    # for i, d in enumerate(block):
    #     sblock += str(d)
    #     pattern = str(file) + '{' + str(fs) + '}'
    #     if re.findall(pattern, sblock):
    #         # print(sblock)
    #         file_indices = [i-j for j in range(block.count(file))]
    #         break
    
    # return file_indices

# function to sort sequences and group spaces in blocks
def sort_and_group_block_spaces(file_space_sequences):
    sorted_file_space_sequences = []

    for block in file_space_sequences:
        # print(block[0])
        # sblock = ''.join(str(d) for d in block)
        # print(sblock)
        # print(re.findall(r'(?<=\.)[0-9]', sblock))
        # print(re.findall(r'(?>\.+)[0-9]', sblock))
        # spaces = [space[:-1] for space in re.findall(r'(?>\.+)[0-9]', sblock)]
        files = get_files_decreasing_order(block)
        # print(files, len(files))

        for file, fs in files.items():
            # s = '.' * fs
            # print(sblock.index(str(file)), block.index(file), file)
            # fi = block.index(file)
            # fi = sblock.index(str(file))
            # spaces = [space[:-1] for space in re.findall(r'(?>\.+)[0-9]', sblock[:fi])]
            # if s in spaces:
            # if spaces:
                # print(sblock, spaces, file)
                # if has_befitting_space(fs, spaces):
                    space_ids = get_space_indices(file, fs, block)
                    file_ids = get_file_indices(file, block)
                    # space = sblock.index(s)
                    # fi = block.index(file)
                    # print(space, fi, sblock[space:], fs)
                    # print(space_ids, file_ids, fi, len(sblock), len(block), fs, file)
                    print(space_ids, file_ids, len(block), fs, file)
                    # print(get_space_indices(fs, block), get_file_indices(file, fs, block))
                    for sid, fid in zip(space_ids, file_ids):
                        block[sid] = file
                        block[fid] = '.'

                    # sblock = ''.join(str(d) for d in block)
                    # spaces = [space[:-1] for space in re.findall(r'(?>\.+)[0-9]', sblock)]
                    # print(sblock, file)
            # print(sblock, spaces, file)
            



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
data = get_data('input_test') # get test data
# data = get_data('input') # get actual data

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

