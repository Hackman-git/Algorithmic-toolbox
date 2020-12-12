# Uses python3
import sys
import math

def get_change(n):
    
    num = 0
    rem = 0
    if n < 5:
        return n
    if n >4 and n < 10:
        rem = n
    if(math.floor(n/10) >= 1):
        num += math.floor(n/10)
        rem = n % 10
    if(math.floor(rem/5) >= 1):
        num += math.floor(rem/5)
        rem = rem % 5
    num += rem

    return num

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
