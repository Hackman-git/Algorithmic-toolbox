#Uses python3

import sys

def max_dot_product(profit, clicks):
    profit.sort(reverse=True)
    clicks.sort(reverse = True)
    res = 0
    for x,y in zip(profit,clicks):
        res += x*y

    return res
if __name__ == '__main__':
    n = int(input())
    profit = list(map(int, input().split()))
    clicks = list(map(int, input().split())) 
    print(max_dot_product(profit, clicks))
    