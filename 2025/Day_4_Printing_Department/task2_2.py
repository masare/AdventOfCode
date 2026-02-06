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
    print(bank)
    # print(hbi, len(bank_str), len(bank_copy), b_len, '---------')
    r_len: int = 12
    def reset_bank(r_len, hbi):
        len_rb: int = len([i for i in bank_copy[hbi:] if i > '0'])
        
        # if hbi == len(bank)-1:
        #     return r_len
        if len_rb >= r_len:
            bank_copy[:hbi] = ['0' for i in bank_copy[:hbi]]
            # print('------------')
        elif len_rb < r_len:
            bank_str[hbi:] = bank[hbi:]
            bank_copy[hbi:] = ['0' for i in range(len_rb)]
            r_len -= len_rb
            # print('=========')

        return r_len
    r_len = reset_bank(r_len, hbi)
    # print(''.join(i for i in bank_copy))
    
    while r_len > 0:
        hbi = bank_copy.index(max(bank_copy))
        rbl: int = reset_bank(r_len, hbi)
        # print(r_len, rbl, '-------',hbi, bank[hbi])
        if r_len > rbl:
            r_len = rbl
        else:
            bank_str[hbi] = bank_copy[hbi]
            bank_copy[hbi] = '0'
            r_len -= 1
        
    # for i in range(r_len):
    #     hbi = bank_copy.index(max(bank_copy))
    #     # print(hbi, len(bank_str), len(bank_copy), b_len)
    #     bank_str[hbi] = bank_copy[hbi]
    #     bank_copy[hbi] = '0'
     
    # if hbi == b_len-1 or hbi == 0:
    #     bank_str[hbi] = bank[hbi]
    #     bank_copy[hbi] = '0'
    #     for i in range(11):
    #         hbi = bank_copy.index(max(bank_copy))
    #         bank_str[hbi] = bank[hbi]
    #         bank_copy[hbi] = '0'
    # elif len(bank[hbi:]) > 11:
    #     bank_str = bank_str[hbi:]
    #     bank_copy = bank_copy[hbi:]
    #     # print(bank)
    #     # def get_next(bank_s, bank_c):
    #     r_len: int = 12
    #     # while len(bank_str) - bank_str.count('0') < 12:
    #     for i in range(12):
    #         hbi = bank_copy.index(max(bank_copy))
    #         bank_str[hbi] = bank_copy[hbi]
    #         bank_copy[hbi] = '0'
    #         r_len -= 1
    #         if len(bank_copy[hbi+1:]) > r_len:
    #             bank_copy[:hbi] = ['0' for b in bank_copy[:hbi]]
    #         elif len(bank_copy[hbi+1:]) < r_len:
    #             bank_str[hbi+1:] = bank_copy[hbi+1:]
    #             bank_copy[hbi+1:] = ['0' for b in bank_copy[hbi+1:]]
    #             r_len -= len(bank_str[hbi+1:])
    #         else:
    #             bank_str[hbi+1:] = bank_copy[hbi+1:]
    #             r_len = 0

    #         if r_len == 0:
    #             break
    #         # if len(bank[hbi+1:]) + (len(bank_str) - bank_str.count('0')) < 12:
    #         #     print(len(bank_str) - bank_str.count('0'),'======',''.join(bank_copy[hbi+1:]))
            
    #         # print(''.join(i for i in bank_str if i > '0'),'-------',''.join(i for i in bank_copy if i > '0'))
    # elif len(bank[hbi:]) < 12:
    #     init_len = len(bank[hbi:])
    #     n_iter: int = 12 - init_len
    #     bank_str[hbi:] = bank_copy[hbi:]
    #     bank_copy[hbi:] = ['0' for i in range(init_len)]
    #     # print(init_len, n_iter, bank[hbi:], bank_str)
    #     # print(bank)
    #     for i in range(n_iter):
    #         hbi = bank_copy.index(max(bank_copy))
    #         bank_str[hbi] = bank_copy[hbi]
    #         bank_copy[hbi] = '0'
    #         # print(len([i for i in bank_copy[hbi:] if int(i) != 0]))
    #         bank_copy[:hbi] = ['0' for i in bank_copy[:hbi]]
            # print(''.join(i for i in bank_str if i > '0'),'-------',''.join(i for i in bank_copy if i > '0'))

    # print(bank_str)
    print(''.join(i for i in bank_str if i > '0'))


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