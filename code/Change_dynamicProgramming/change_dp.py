# Uses python3
import sys

def get_change(amount):
    coins = [1,3,4]
    coinReqd = [0] * (amount + 1)
    for i in range(1, amount+1):
        coinReqd[i] = 100000
        for j in coins:
            if j <= i:
                coinReqd[i] = min(coinReqd[i - j] + 1, coinReqd[i])
            else:
                continue

    return coinReqd[amount]


if __name__ == '__main__':
    amount = int(input())
    print(get_change(amount))
