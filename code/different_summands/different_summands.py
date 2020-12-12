# Uses python3
import sys

def optimal_summands(n):
    summands = []
    current_sum = 0
    for i in range(1, n+1):
        summands.append(i)
        if (summands[i-1] + current_sum) < n:
            current_sum += summands[i-1]
            continue
        elif (current_sum + summands[i-1]) == n:
            break
        else:
            diff = (current_sum + summands[i-1]) - n
            if diff in summands:
                summands.remove(diff)
                break

    return summands

if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
