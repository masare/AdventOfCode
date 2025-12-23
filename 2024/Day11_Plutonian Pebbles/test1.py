import re

# function to remove extra leading zeros
def post_process_stone(stone: str) -> str:
    # print(re.sub(r"0+$", '0', stone)) # remove trailing zeros
    # print(re.sub(r"^0+", '', stone)) # remove leading zeros
    # stone = re.sub(r"^0+", '', stone)
    # print(stone) 
    if len(re.findall(r"^0+[1-9]+", stone)) > 0:
        return re.sub(r"^0+", '', stone)
    else:
        return re.sub(r"0+$", '0', stone)
    

# function to appropriate blink results of stones
def present_blink(stones: list[str], blinks: int =1) -> list[str]:
    stones_copy = stones.copy() # create a copy of input data to avoid possible corruption of original data

    for i in range(blinks): # blink n times
        blink_results = [] # a container to keep record new stones after a blink

        for new_stone in map(blink, stones_copy): # make a blink on current state of stones
            for stone in new_stone: # iterate over results of each individual stone's blink
                # post_process_stone(stone)
                blink_results.append(stone) # extract new stones formed
            # blink_results.extend(new_stone)

        stones_copy = blink_results.copy() # reset the current state of stones
        # del blink_results # free memory of blink results
        # print(f"After {i+1} blinks:", stones_copy, sep='\n', end='\n\n')

    stones = stones_copy # update state of original stones after successful blinks

    return stones 


# function to chane stone
def change_stone(stone:str) -> list[str]:
    return [str(int(stone) * 2024)]


# function to split stone
def split_stone(stone:str) -> list[str]:
    half_stone = len(stone)//2
    stones = [stone[:half_stone], stone[half_stone:]]
    return [post_process_stone(s) for s in stones]

# function to blink a stone
def blink(stone: str) -> list[str]:
    if stone == '0':
        return ['1']
    
    if len(stone) % 2 > 0:
        # return [str(int(stone) * 2024)]
        return change_stone(stone)
    else:
        # half_stone = len(stone)//2
        # return [post_process_stone(s) for s in [stone[:half_stone], stone[half_stone:]]]
        return split_stone(stone)

# function to get data
def get_data(path: str) -> list[str]:
    with open(path, 'r') as file:
        return [stone for stone in file.readline().split()]
    
def main() -> None:
    # get data
    stones = get_data('input') # get main test data
    # stones = get_data('input_test') # get sample test data

    # view data
    print(stones)

    # test blink
    # blink_test = [map(blink, stones)]

    # view blink results
    # print(blink_test)

    # make blinks
    blink_data = present_blink(stones, 40)

    # print number of stones after blinks
    print(f"Total Stones after Blinks: {len(blink_data)}")
    # print(f"Stones: {blink_data}")

if __name__ == '__main__':
    main()