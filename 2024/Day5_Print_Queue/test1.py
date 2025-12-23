from statistics import median
rules = {}
rorder = []

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

# get correct orders
with open('input_test.txt', 'r') as file:
# with open('input', 'r') as file:
    mvalue_total = 0
    for line in file.readlines(): #[:1178]:
        line = line.strip()
        if '|' in line:
            new_rule(line)
        elif ',' in line:
            # print(rules)
            line = line.split(',')
            if check_order(line):
                rorder.append(line)
                # print(line[(len(line)-1)//2])
                mvalue_total += int(line[(len(line)-1)//2])
                # mvalue_total += int(median(line))
    #             # print(len(line), line)
    #         # else:
    #             # print('Not', line)
    print(mvalue_total)