from itertools import combinations


# def get_incorrect_expressions(expressions, correct_expressions):
#     incorrect_expressions = {}
#     for answer, operands in expressions.items():
#         if not answer in correct_expressions:
#             incorrect_expressions[answer] = operands

#     return incorrect_expressions

# def get_incorrect_expressions(answers, operands, correct_expressions):
#     incorrect_expressions = {}
#     for i, ans in enumerate(answers):
#         if not ans in correct_expressions:
#             incorrect_expressions[ans] = operands[i]

#     return incorrect_expressions

def check_operation(expression, ops):
    y, x = expression
    ans = x[0]
    # print(x, ops, ans, operators)
    for j, op in enumerate(ops):
        if op == '||':
            ans = str(ans) + x[j+1]
        else:
            ans = str(ans) + op + x[j+1]
        # print(ans, eval(ans))
        ans = eval(ans)
        # print(ans, eval(ans))
    # if ans == y:
    #     return True
    # else:
    #     return False
    return ans == y

def get_correct_expression(expressions, base_operators):
    num_exprs = len(expressions)
    correct_expressions = {}
    incorrect_expressions = {}
    
    for i, expression in enumerate(expressions.items()):
    
        found = get_operators(expression, base_operators) # Get operators combinations
        
        if found:
            correct_expressions[expression[0]] = expression[1]
        else:
            # incorrect_expressions.update(dict([expression]))
            incorrect_expressions[expression[0]] = expression[1]
    # print(y, x, ans, ops)
        print(len(correct_expressions), len(incorrect_expressions), i, num_exprs)

    return correct_expressions, incorrect_expressions

# def get_correct_expression(expressions, base_operators):
#     num_exprs = len(expressions)
#     correct_expressions = {}
#     i = 0
#     for y, x in expressions.items():
#         num_x = len(x)
    
#         operators = get_operators(x, base_operators) # Get operators combinations
        
#         for ops in operators:
#             ans = x[0]
#             # print(x, ops, ans, operators)
#             for j, op in enumerate(ops):
#                 if op == '||':
#                     ans = str(ans) + x[j+1]
#                 else:
#                     ans = str(ans) + op + x[j+1]
#                 # print(ans, eval(ans))
#                 ans = eval(ans)
#                 # print(ans, eval(ans))
#             if ans == y:
#                 if not y in correct_expressions.keys():
#                     correct_expressions[y] = {
#                         'operands' : x,
#                     #     'operators': ops # [ops]
#                     }
#                     # correct_expressions.append(y)
#                 break
#                 # else:
#                     # correct_expressions[y]['operators'].append(ops)
#             # print(y, x, ans, ops)
#         print(len(correct_expressions), i, num_exprs)
#         i+=1

#     return correct_expressions

# def get_correct_expression(answers, operands, base_operators):
#     num_exprs = len(answers)
#     correct_expressions = {}

#     for i in range(num_exprs):
#         y = int(answers[i])
#         x = operands[i]
#         num_x = len(x)
    
#         operators = get_operators(x, base_operators) # Get operators combinations
        
#         for ops in operators:
#             ans = x[0]
#             # print(x, ops, ans, operators)
#             for j, op in enumerate(ops):
#                 if op == '||':
#                     ans = str(ans) + x[j+1]
#                 else:
#                     ans = str(ans) + op + x[j+1]
#                 # print(ans, eval(ans))
#                 ans = eval(ans)
#                 # print(ans, eval(ans))
#             if ans == y:
#                 if not y in correct_expressions.keys():
#                     correct_expressions[y] = {
#                         'operands' : x,
#                     #     'operators': ops # [ops]
#                     }
#                     # correct_expressions.append(y)
#                 break
#                 # else:
#                     # correct_expressions[y]['operators'].append(ops)
#             print(y, x, ans, ops)
#         print(correct_expressions, i, num_exprs)

#     return correct_expressions

# Get all possible operators combination for each expression
def get_operators(expression, base_operators):
    # print(expression)
    num_ops =  len(expression[1]) - 1
    # opd_operators = set([*combinations(base_operators * num_ops, num_ops)])
    opd_operators = set(combinations(base_operators * num_ops, num_ops))
    for ops in opd_operators:
        if check_operation(expression, ops):
            return True
        # opd_operators.append(ops)
        # opd_operators = list(set(opd_operators)) 
    # print(opd_operators)
    # operators.append(opd_operators)
    # print(operators)
    return False

# # Get all possible operators combination for each expression
# def get_operators(operands, base_operators):
#     # operators = []
#     # base_operators = ['+', '*', '||']

#     # Get the number of operators needed per expression
#     # for opds in operands:
#     num_ops =  len(operands) - 1
#     opd_operators = []
#     for ops in combinations(base_operators * num_ops, num_ops):
#         opd_operators.append(ops)
#         opd_operators = list(set(opd_operators)) 
#     # print(opd_operators)
#     # operators.append(opd_operators)
#     # print(operators)
#     return opd_operators

# Get data from file
def get_data(path):
    expressions = {}
    with open(path, 'r') as file:
        # answers = []
        # operands = []
        
        for line in file.readlines():
            ans, opds = line.strip().split(': ')
            # answers.append(ans)
            # operands.append(opds.split(' '))
            expressions[int(ans)] = opds.split(' ')
    
    # return answers, operands
    return expressions

# Get data
# answers, operands = get_data('input_test') # test data
# answers, operands = get_data('input') # actual data

# expressions = get_data('input_test') # actual data
expressions = get_data('input') # actual data

# Get operators combinations
# operators = get_operators(operands)

# Initial base operators for simple operations
base_operators = ['+', '*']

# Get correct expressions with simple operations
# so_correct_expressions = get_correct_expression(answers, operands, base_operators)
so_correct_expressions, incorrect_expressions = get_correct_expression(expressions, base_operators)

# Get incorrect expressions with simple operations
# incorrect_expressions = get_incorrect_expressions(answers, operands, so_correct_expressions.keys())
# incorrect_expressions = get_incorrect_expressions(expressions, so_correct_expressions.keys())

# Reinitialize base operators for complex operations
base_operators = ['+', '*', '||']

# Get correct expressions with complex operations
# co_correct_expressions = get_correct_expression(incorrect_expressions.keys(), incorrect_expressions.values(), base_operators)
co_correct_expressions, _ = get_correct_expression(incorrect_expressions, base_operators)

# # Print out total sum of independent values of correct expressions
print(sum(so_correct_expressions.keys()), sum(co_correct_expressions.keys()), sum(so_correct_expressions.keys()) + sum(co_correct_expressions.keys()))
# print(sum(correct_expressions))