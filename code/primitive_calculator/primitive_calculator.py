# Uses python3
import sys

def optimal_sequence(n):


    all_nums = [0,0,1]
    if n > 2:
        for i in range(3, n+1):
            a,b,c = 0,0,0
            if i % 3 == 0:
               a = i // 3
            if i % 2 == 0:
               b = i // 2
            c = i - 1

            if a == 0 and b == 0:
                m = all_nums[c] + 1
            elif a == 0:
                m = min(all_nums[b] + 1, all_nums[c] + 1)
            elif b == 0:
                m = min(all_nums[a] + 1, all_nums[c] + 1)
            else:
                m = min(all_nums[a] + 1, all_nums[b] + 1, all_nums[c] + 1)

            all_nums.append(m)
        
    return all_nums[n]

n = int(input())
minimum = optimal_sequence(n)
print(minimum)

