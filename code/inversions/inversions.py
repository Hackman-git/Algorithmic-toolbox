# Uses python3
import sys
import math
number_of_inversions = 0

def get_number_of_inversions(a):
    global number_of_inversions
    # if right - left <= 1:
    #     return number_of_inversions
    if len(a) > 1:

        mid = len(a)//2
        lefthalf = a[:mid]
        righthalf = a[mid:]
        get_number_of_inversions(lefthalf)
        get_number_of_inversions(righthalf)
        #write your code here

        i=0
        j=0
        k=0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                a[k]=lefthalf[i]
                i=i+1
            else:
                a[k]=righthalf[j]
                number_of_inversions += (len(lefthalf) - i)
                j=j+1
            k=k+1


        while i < len(lefthalf):
            a[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            a[k]=righthalf[j]
            j=j+1
            k=k+1


if __name__ == '__main__':
    n = input()
    a = list(map(int, input().split()))
    # b = n * [0]
    get_number_of_inversions(a)
    print(number_of_inversions)
