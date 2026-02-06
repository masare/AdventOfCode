from itertools import combinations
from typing import Generator
import numpy as np

# BANKS_TXT: str = "test.txt"
BANKS_TXT: str = "input.txt"

def bank_battery_finder(bank: str) -> str:
    # print(bank, '------')
    # b_len: int = len(bank)
    # best_pair: tuple = (1,2) # stores positions of best battery combo
    max_cap: str = bank[:12] # stores max battery capacity for bank

    # for i in range(b_len):
        # bat_comb = [*combinations(bank[i:],2)][:b_len-(i+1)]
        # print(bat_comb)
        # if bank[i] > max(bank[i+1:]):
        #     break
    
    # index of highest battery capacity on bank
    hbi: int = np.argmax(np.array([int(b) for b in bank]))
    # best_pair: str = '0'
    if hbi == len(bank)-1:
        bat_comb = [''.join(bat) for bat in set(combinations(bank[:hbi+1],12))]
        # best_pair = max(bank[:hbi])
        # max_cap = best_pair + bank[hbi]
    elif hbi == 0:
        bat_comb = [''.join(bat) for bat in set(combinations(bank[:],12))]
    elif len(bank[hbi:]) - hbi > 12:
        bat_comb = [''.join(bat) for bat in set(combinations(bank[hbi:],12))]
    else: 
        bat_comb = [''.join(bat) for bat in set(combinations(bank[:],12))]
        # best_pair = max(bank[hbi+1:])
        # max_cap = bank[hbi] + best_pair
        # print(max(''.join(bat) for bat in set(combinations(bank[:],12))))

    max_cap = max(bat_comb)    
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