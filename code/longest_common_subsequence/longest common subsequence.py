#Uses python3

def lcs2(a_list, b_list):
    m = len(b_list)
    n = len(a_list)
    dp_table = [[None]* (n+1) for i in range (m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp_table[i][j] = 0
            elif a_list[j-1] == b_list[i-1]:
                dp_table[i][j] = dp_table[i-1][j-1] + 1
            else:
                dp_table[i][j] = max(dp_table[i-1][j], dp_table[i][j-1])

    index = dp_table[m][n]
    lcs = [''] * index
    
    i = m
    j = n

    while i > 0 and j > 0:
        if a_list[j-1] == b_list[i-1]:
            lcs[index - 1] = a_list[j-1]
            i -= 1
            j -= 1
            index -= 1
        elif dp_table[i-1][j] < dp_table[i][j-1]:
            j -= 1

        else:
            i -= 1

    # print(''.join(lcs))
    
    return dp_table[m][n]

if __name__ == '__main__':
    a = int(input())
    a_list = list( input().split())
    b = int(input())
    b_list = list(input().split())

    print(lcs2(a_list, b_list))
