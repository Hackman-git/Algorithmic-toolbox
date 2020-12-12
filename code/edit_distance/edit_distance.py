# Uses python3
def edit_distance(s, t):
    a_list = list(s)
    b_list = list(t)
    m = len(b_list)
    n = len(a_list)
    dp_table = [[None]* (n+1) for i in range (m + 1)]
    for i in range(m+1):
        for j in range(n+1):
            dp_table[i][0] = i
            dp_table[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            insertion = dp_table[i][j-1] + 1
            deletion = dp_table[i-1][j] + 1
            match = dp_table[i-1][j-1]
            mismatch = dp_table[i-1][j-1] +1

            if a_list[j-1] == b_list[i-1]:
                dp_table[i][j] = min(insertion, deletion, match)
            else:
                dp_table[i][j] = min(insertion, deletion, mismatch)

    index = dp_table[m][n]
    return index



if __name__ == "__main__":
    s = input()
    t = input()
    print(edit_distance(s, t))
