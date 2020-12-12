# Uses python3
from sys import stdin

def fibonacci_sum_squares(n):
    if n <= 1:
        return n
    else:
        return ( (get_fibonacci_last_digit(n) * get_fibonacci_last_digit(n+1)) % 10)

def get_fibonacci_last_digit(n):
    # arr = [1,1]
    if (n <= 1):
        return n

    else:
        last_digits = [0]*60
        last_digits[0] = 0
        last_digits[1] = 1

        for i in range(2, 60):
            last_digits[i] = (last_digits[i-1] + last_digits[i-2]) % 10

        return last_digits[n % 60]

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
