# Uses python3
import sys

def gcd_naive(a, b):
    if (a == 0):
        return b
    elif (b ==0):
        return a
    else:
        return gcd_naive(min(a,b),max(a,b)%min(a,b))

def lcm_naive(a, b):
    x = gcd_naive(a,b)
    y = int(int(a/x)*int(b/x))
    return x*y

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm_naive(a, b))

