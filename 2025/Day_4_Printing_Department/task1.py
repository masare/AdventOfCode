from typing import Generator
from collections.abc import Iterator
import numpy as np

# ROLLS_TXT: str = "test.txt"
ROLLS_TXT: str = "input.txt"

def forklift(rolls: str) -> str:
    access_rolls:str = ''
    

    return access_rolls

def read_file(file_path) -> list[str]:
    field: list[str] = []
    with open(file_path, 'r') as f:
        for rolls in f.readlines():
            field.append(rolls.strip())

    return field

def main() -> None:
    data: list[str] = read_file(ROLLS_TXT)
    # print(data)

    field = np.ones((len(data)+2, len(data[0])+2)) # add buffer rows and columns at the top, bottom, left, and right.

    # print(len(data[0]), len(data), field.shape)

    # set buffer areas to 0
    field[0,:] = 0
    field[-1,:] = 0
    field[:, 0] = 0
    field[:, -1] = 0

    # print(field)

    # set cells not containing rolls to 0
    # field[1:-1, 1:-1] = 
    # print([i for i in list([list(row) for row in data])])
    print([roll if roll == '@' else len(roll) for roll in list([list(row) for row in data])])
    # print([1 if roll == '@' else 0 for roll in list([list(row) for row in data])])

    # print(field[1:-1, 1:-1])
    # bank_max_vals: Generator[str, None, None] = (bank_battery_finder(bank) for bank in data)
    # # print([*bank_max_vals]) 

    # print(sum(int(bat) for bat in bank_max_vals))
        


if __name__ == "__main__":
    main()