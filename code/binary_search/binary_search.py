# Uses python3
import sys
import math

def binary_search(a,left,right,x):
    if left > right:
        return -1
    mid = math.floor(left + ((right - left) / 2))
    if x == a[mid]:
        return mid
    elif x < a[mid]:
        return binary_search(a,left,mid-1,x)
    else:
        return binary_search(a,mid+1,right,x)

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    data = list(map(int, input().split()))
    n = data[0]
    data2 = list(map(int, input().split()))
    k = data[0]
    a = data[1 : n + 1]
    left, right = 0, len(a)-1
    for x in data2[1:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a,left,right, x), end = ' ')
