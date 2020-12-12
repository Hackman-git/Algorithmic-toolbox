# Uses python3
import sys

def optimal_weight(W, weights, n):
    vals = weights[:]
    dp_table = [[0]*(W+1) for i in range (n + 1)]

    for i in range(1, n+1):
        for w in range(1, W+1):
            dp_table[i][w] = dp_table[i-1][w]
            if weights[i-1] <= w:
                v = dp_table[i-1][w - weights[i-1]] + vals[i-1]
                if dp_table[i][w] < v:
                    dp_table[i][w] = v

    return dp_table[n][W]


if __name__ == '__main__':
    cap_and_n = list(map(int,input().split()))
    W = cap_and_n[0]
    n = cap_and_n[1]
    weights = list(map(int,input().split()))
    print(optimal_weight(W, weights,n))
