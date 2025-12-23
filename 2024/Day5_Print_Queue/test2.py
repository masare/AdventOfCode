import numpy as np
rules = {}
rorders = []
corders = []

# add or update a rule
def new_rule(data):
    key, value = data.split('|')
    if (key in rules.keys()) and (not (value in rules[key])):
        rules[key].append(value)
    else:
        rules[key] = [value]

# check whether order is correct or not
def check_order(order):
    order_len = len(order)
    for ind in range(order_len-1):
        page = order[ind]
        if page not in rules.keys():
            # print('--------------------------',order)
            return False
        
        page_rule = set(rules[page])
        rm_order = set(order[ind+1:])
        common = page_rule.intersection(rm_order)
        # print('+++++', order, page_rule, rm_order, common)
        if not len(common) == len(rm_order):
            # print('=====', order, page_rule, rm_order, common)
            return False
        # if not order[ind+1] in page_rule:
            # return False
        # for i in range(ind+1, order_len):
        #     if not (order[i] in page_rule):
        #         return False
        # print(page, page_rule)
    return True

def fix_order(order):
    order_len = len(order)
    # print(order_len, '=========', order)
    for ind in range(order_len-1):
        # print(order_len, ind, order, len(order))
        page = order[ind]
        if page not in rules.keys():
            order.remove(page)
            order.append(page)
            continue

        page_rule = set(rules[page])
        rm_order = set(order[ind+1:])
        # if len(rm_order) > 1 and isinstance(rm_order, list):
        #     rm_order = set(rm_order)
        # else:
        #     rm_order = set(rm_order)
        # print(rm_order)
        uncommon = rm_order.difference(page_rule)
        # print(uncommon, rm_order, page_rule)
        if len(uncommon) == 1:
            unk_page = list(uncommon)[0]
            order.remove(unk_page)
            order.insert(ind, unk_page)
            # print(order, '--------')
        elif len(uncommon) == 2:
            unk_pages = list(uncommon)
            order.remove(unk_pages[0])
            order.remove(unk_pages[1])
            if unk_pages[1] in rules[unk_pages[0]]:
                order.insert(ind, unk_pages[0])
                order.insert(ind+1, unk_pages[1])
            else:
                order.insert(ind, unk_pages[1])
                order.insert(ind+1, unk_pages[0])
        elif len(uncommon) > 2:
            order = order[:ind+1] + fix_order(list(rm_order))

    # print(order, '--------')
    # if check_order(order):
    #     return order
    # else:
    #     return fix_order(order)
    return order


def get_midvalue_total(orders):
    mvalue_total = 0
    for order in orders:
        print(order, int(order[(len(order)-1)//2]), len(order))
        mvalue_total += int(order[(len(order)-1)//2])

    return mvalue_total

def print_rules():
    for rule in rules.items():
        print(rule) 

# get correct orders
# with open('input_test.txt', 'r') as file:
with open('input', 'r') as file:
    # mvalue_total = 0
    for line in file.readlines(): #[:1178]:
        line = line.strip()
        if '|' in line:
            new_rule(line)
        elif ',' in line:
            # print(rules)
            line = line.split(',')
            if check_order(line):
                rorders.append(line)
                # mvalue_total += int(line[(len(line)-1)//2])
            else:
                # fix_order(line)
                corders.append(fix_order(line))
                print('Not', line)
    
    # print_rules()
    # print(mvalue_total)
    # print(f'Right Orders Midvalue Total: {get_midvalue_total(rorders)}')
    print(f'Corrected Orders Midvalue Total: {get_midvalue_total(corders)}')
