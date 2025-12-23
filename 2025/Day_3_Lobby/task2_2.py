from itertools import combinations, repeat
from typing import Generator
import numpy as np

BANKS_TXT: str = "test.txt"
# BANKS_TXT: str = "input.txt"

def bank_battery_finder(bank: str) -> str:
    # print(bank, '------')
    # b_len: int = len(bank)
    best_pair: list[int] = [*repeat(0, 12)] # stores positions of best battery combo
    max_cap: str = '000000000000' # stores max battery capacity for bank
    bank_l = list(bank)
    for i in range(12):
        hbi: int = np.argmax(np.array(bank_l))
        best_pair[i] = hbi
        bank_l[hbi] = '0'

    
    max_cap = ''.join(bank[i] for i in sorted(best_pair)) 

    print(bank, max_cap)

    # print(bank, hbi, best_pair, max_cap)
    

    return max_cap

def read_file(file_path) -> Generator[str, None, None]:
    with open(file_path, 'r') as f:
        for batteries in f.readlines():
            yield batteries.strip()

def main() -> None:
    data: Generator[str, None, None] = read_file(BANKS_TXT)
    # print(list(data))
    # print(len(data))
    # for bank in data:
    #     bank_battery_finder(bank)
    #     break

    bank_max_vals: Generator[str, None, None] = (bank_battery_finder(bank) for bank in data)
    # print([*bank_max_vals]) 

    print(sum(int(bat) for bat in bank_max_vals))
        


if __name__ == "__main__":
    main()