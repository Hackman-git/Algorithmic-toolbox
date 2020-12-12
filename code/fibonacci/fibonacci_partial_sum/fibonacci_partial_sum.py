# Uses python3
import sys

def fibonacci_partial_sum(from_, to):
    if(from_ == 0):
        before_f = 0
    else:
        before_f = fibonacci_sum(from_ - 1)
    t = fibonacci_sum(to)
    if from_ == to:
        return get_fibonacci_last_digit(from_)
    elif t < before_f:
        return ((t+10) - before_f)
    else:
        return t - before_f


def fibonacci_sum(n):
    if n <= 1:
        return n
    else:
        last = get_fibonacci_last_digit(n+2)
        if last == 0:
            return 9
        else:
            return last - 1


def get_fibonacci_last_digit(n):
    if (n <= 1):
        return n

    else:
        arr = [0]*60
        arr[0] = 0
        arr[1] = 1

        for i in range(2, 60):
            arr[i] = (arr[i-1] + arr[i-2]) % 10

        return arr[n % 60]

if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum(from_, to))