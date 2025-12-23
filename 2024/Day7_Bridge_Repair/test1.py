from itertools import combinations


def get_correct_expression(answers, operands, operators):
    num_exprs = len(answers)
    correct_expressions = {}

    for i in range(num_exprs):
        y = int(answers[i])
        x = operands[i]
        num_x = len(x)
        for ops in operators[i]:
            # x_copy = x[:]
            ans = x[0]
            # print(x, x_copy, ans)
            for j, op in enumerate(ops):
                ans = str(ans) + op + x[j+1]
                # print(ans, eval(ans))
                ans = eval(ans)
                # print(ans, eval(ans))
                if ans == y:
                    if not y in correct_expressions.keys():
                        correct_expressions[y] = {
                            'operands' : x,
                            'operators': [ops]
                        }
                    else:
                        correct_expressions[y]['operators'].append(ops)
        # print(y, x, num_x, operators[i])
    # print(correct_expressions)

    return correct_expressions


# Get all possible operators combination for each expression
def get_operators(operands):
    operators = []
    base_operators = ['+', '*']

    # Get the number of operators needed per expression
    for opds in operands:
        num_ops =  len(opds) - 1
        opd_operators = []
        for ops in combinations(base_operators * num_ops, num_ops):
            opd_operators.append(ops)
        # print(opd_operators)
        operators.append(list(set(opd_operators)))
    # print(operators)
    return operators

# Get data from file
def get_data(path):
    with open(path, 'r') as file:
        answers = []
        operands = []
        
        for line in file.readlines():
            ans, opds = line.strip().split(': ')
            answers.append(ans)
            operands.append(opds.split(' '))
    
    return answers, operands

# Get data
# answers, operands = get_data('input_test') # test data
answers, operands = get_data('input') # actual data

# Get operators combinations
operators = get_operators(operands)

# Get correct expressions
correct_expression = get_correct_expression(answers, operands, operators)

# Print out total sum of independent values of correct expressions
print(sum(correct_expression.keys()))