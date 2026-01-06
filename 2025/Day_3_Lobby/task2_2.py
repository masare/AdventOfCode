from itertools import combinations
from typing import Generator
import numpy as np

# BANKS_TXT: str = "test.txt"
BANKS_TXT: str = "input.txt"

def bank_battery_finder(bank: str) -> str:
    # print(bank, '------')
    b_len: int = len(bank)
    # best_pair: tuple = (1,2) # stores positions of best battery combo
    max_cap: str = bank[:12]#''.join('0' for i in range(len(bank))) # stores max battery capacity for bank

    bank_str: list[str] = ['0' for i in range(b_len)]
    bank_copy: list[str] = [i for i in bank]
    hbi: int = bank_copy.index(max(bank_copy))

        
    if hbi == b_len-1 or hbi == 0:
        bank_str[hbi] = bank[hbi]
        bank_copy[hbi] = '0'
        for i in range(11):
            hbi = bank_copy.index(max(bank_copy))
            bank_str[hbi] = bank[hbi]
            bank_copy[hbi] = '0'
    elif len(bank[hbi:]) > 11:
        bank_str = bank_str[hbi:]
        bank_copy = bank_copy[hbi:]
        for i in range(11):
            hbi = bank_copy.index(max(bank_copy))
            bank_str[hbi] = bank_copy[hbi]
            bank_copy[hbi] = '0'
    elif len(bank[hbi:]) < 12:
        init_len = len(bank[hbi:])
        n_iter: int = 12 - init_len
        bank_str[hbi:] = bank_copy[hbi:]
        bank_copy[hbi:] = ['0' for i in range(init_len)]
        # print(init_len, n_iter, bank[hbi:], bank_str)
        for i in range(n_iter):
            hbi = bank_copy.index(max(bank_copy))
            bank_str[hbi] = bank_copy[hbi]
            bank_copy[hbi] = '0'


    # print(bank_str)
    # print(''.join(i for i in bank_str if i > '0'))


    max_cap = ''.join(i for i in bank_str if i > '0')
    # max_cap = max(bat_comb)    
    # print(bank, bat_comb, max(bat_comb))
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