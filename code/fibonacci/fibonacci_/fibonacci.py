# Uses python3
def calc_fib(n):
    arr = [1,1]
    if (n <= 1):
        return n
    else:
        for i in range(n-2):
            arr.append(arr[len(arr)-1] + arr[len(arr)-2])
        return arr[-1]

n = int(input())
print(calc_fib(n))
