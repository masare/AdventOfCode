from typing import Generator

ROTATIONS_TXT: str = "input.txt"

def invalid_ids_finder(ids_range: str) -> tuple[list[str], int]:
    invalid_ids: list[str] = []
    inv_id_count: int = 0
    ids: list = ids_range.split('-')
    for id in range(int(ids[0]), int(ids[1])):
        id_s: str = str(id)
        id_l: int = len(id_s)
        # for id_p in range(id_l//2, 0, -1):
        for id_p in range(1, (id_l//2)+1):
        # for id_p in range(id_l-1, 0, -1):
            id_pc: int = id_s.count(id_s[:id_p])
            # print(id_s, id_s[:id_p], id_pc, len(id_s[:id_p]), id_pc*len(id_s[:id_p]), id_l)
            if id_pc >= 2:
                if id_pc*len(id_s[:id_p]) == id_l:
                    # print(id_s, id_s[:id_p], id_pc, len(id_s[:id_p]), id_pc*len(id_s[:id_p]), id_l)
                    invalid_ids.append(id_s)
                    inv_id_count += 1
                    break
        # if (id_l % 2 == 0):
        #     if id_s[:id_l//2] == id_s[id_l//2:]:
        #         # print(id_s, '--------')
        #         invalid_ids.append(id_s)
        #         inv_id_count += 1


    return invalid_ids, inv_id_count

def read_file(file_path) -> Generator[tuple[list[str], int], None, None]:
    with open(file_path, 'r') as f:
        data: str = f.readlines()[0]
        # print(data)
        # print(len(data))
        for id_range in data.split(','):
            # print(id_range)
            # _range: list = id_range.split('-')
            # low: int = int(_range[0])
            # high: int = int(_range[1])
            # curr_id: str = _range[0]
            yield invalid_ids_finder(id_range)

def main() -> None:
    invalid_ids: list[str] = []
    invalid_ids_count: int = 0
    invalids:Generator[tuple[list[str], int], None, None] = read_file(ROTATIONS_TXT)
    
    for invalid in invalids:
        invalid_ids.extend(invalid[0])
        invalid_ids_count += invalid[1]
    # print(invalids, '=========')
    # break
    print(invalid_ids)
    print(sum([int(id) for id in invalid_ids]))


if __name__ == "__main__":
    main()