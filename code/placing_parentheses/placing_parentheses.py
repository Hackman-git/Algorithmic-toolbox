# Uses python3
import math

def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(numbers, operations):
    global M, m
    n = len(numbers)
    for i in range(1, n+1):
        m[i][i] = int(numbers[i-1])
        M[i][i] = int(numbers[i-1])
    
    for s in range(1, n):
        for i in range(1, n - s + 1):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(i, j)

    return M[1][n]

def MinAndMax(i,j):
    global M, m, numbers, operations
    minimum = math.inf
    maximum = -math.inf

    for k in range(i, j):
        a = evaluate(M[i][k], M[k+1][j], operations[k-1])
        b = evaluate(M[i][k], m[k+1][j], operations[k-1])
        c = evaluate(m[i][k], M[k+1][j], operations[k-1])
        d = evaluate(m[i][k], m[k+1][j], operations[k-1])

        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)

    return (minimum, maximum)

if __name__ == "__main__":
    numbers = []
    operations = []
    expression = input()
    i = 0
    j = 1
    while i < len(expression):
        numbers.append(expression[i])
        i += 2
    while j < len(expression):
        operations.append(expression[j])
        j += 2

    M = [[None] * (len(numbers)+1) for i in range(len(numbers) + 1)]
    m = [[None] * (len(numbers)+1) for i in range(len(numbers) + 1)]

    # print(numbers)
    # print(operations)
    print(get_maximum_value(numbers, operations))