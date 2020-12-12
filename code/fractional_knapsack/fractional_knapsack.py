# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.0
    n = len(weights)
    ratios = []
    for i in range(n):
        ratios.append(values[i]/weights[i])
    for i in range(n):
        if capacity == 0:
            return value
        else:
            max_ratio = max(ratios)
            index = ratios.index(max_ratio)
            a = min(weights[index],capacity)
            value += a * (values[index] / weights[index])
            ratios[index] = 0
            capacity -= a

    return value


if __name__ == "__main__":
    data = list(map(int, input().split()))
    n, capacity = data[0:2]
    values = []
    weights = []
    for i in range(n):
        leest = list(map(int, input().split()))
        values.append(leest[0])
        weights.append(leest[1])

    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
