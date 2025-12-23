from itertools import combinations
from typing import Generator
import numpy as np

# BANKS_TXT: str = "test.txt"
BANKS_TXT: str = "input.txt"

def bank_battery_finder(bank: str) -> str:
    # print(bank, '------')
    # b_len: int = len(bank)
    # best_pair: tuple = (1,2) # stores positions of best battery combo
    max_cap: str = bank[:2] # stores max battery capacity for bank

    # for i in range(b_len):
        # bat_comb = [*combinations(bank[i:],2)][:b_len-(i+1)]
        # print(bat_comb)
        # if bank[i] > max(bank[i+1:]):
        #     break
    # for i, bat in enumerate(bank, 1):
    #     # print(np.array([int(b) for b in bank[i:]]))
    #     # break
    #     bp: int = np.argmax(np.array([int(b) for b in bank[i:]]))
    #     value = bank[i-1] + bank[i+bp]
    #     print(bank, i, bat, bp, value)
    #     # print(bat, bp)

    #     if bat > max(bank[i:]) or i == (b_len-1):
    #         break
    # index of highest battery capacity on bank
    hbi: int = np.argmax(np.array([int(b) for b in bank]))
    best_pair: str = '0'
    if hbi == len(bank)-1:
        best_pair = max(bank[:hbi])
        max_cap = best_pair + bank[hbi]
    else:
        best_pair = max(bank[hbi+1:])
        max_cap = bank[hbi] + best_pair

    # print(bank, hbi, best_pair, max_cap)
    
    # index of the second highest on the left of the highest
    # hb_bhbi: int = -1000000
    # lhb: str = '0'
    # if hbi > 0:
    #     hb_bhbi = np.argmax(np.array([int(b) for b in bank[:hbi]]))
    #     lhb = max(bank[:hbi])
    # # index of the second highest on the right of the highest
    # hb_ahbi: int = -1000000
    # rhb: str = '0'
    # if hbi < len(bank)-1:
    #     # print(len(bank[hbi+1:]), max(bank[hbi+1:]))
    #     hb_ahbi = np.argmax(np.array([int(b) for b in bank[hbi+1:]]))
    #     rhb = max(bank[hbi+1:])

    # if (hb_bhbi > -1000000) and (hb_ahbi > -1000000):
    #     # if bank[hb_bhbi] > bank[hb_ahbi]:
    #     if lhb > rhb:
    #         # max_cap = bank[hb_bhbi] + bank[hbi] 
    #         max_cap = lhb + bank[hbi]
    #     # elif bank[hb_bhbi] == bank[hb_ahbi]:

    #     else:
    #         # max_cap = bank[hbi] + bank[hb_ahbi]
    #         max_cap = bank[hbi] + rhb
    # elif hb_bhbi > -1000000 and hb_ahbi == -1000000:
    #     # max_cap = bank[hb_bhbi] + bank[hbi]
    #     max_cap = lhb + bank[hbi] 
    # else:
    #     # max_cap = bank[hbi] + bank[hb_ahbi]
    #     max_cap = bank[hbi] + rhb

    # print(bank, hb_bhbi, hbi, hb_ahbi, max_cap)
    # print(lhb, rhb)
    # print(bank, hbi, bank[hbi], hb_bhbi, bank[hb_bhbi], hb_ahbi, bank[hb_ahbi])
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