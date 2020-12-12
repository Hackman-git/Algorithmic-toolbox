# Uses python3
my_dict =  {}
current_sum = 0

def get_majority_element(arr):
    global my_dict,current_sum,l
    if len(arr) > 1:
        mid = len(arr) // 2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        get_majority_element(lefthalf)
        get_majority_element(righthalf)

    else:
        my_dict[arr[0]] += 1
        current_sum += 1
    if current_sum == l:
        return

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    l = len(a)
    my_set = set(a)
    for items in my_set: 
        my_dict[items] = 0
    get_majority_element(a)
    maximum = max(my_dict.values())
    if maximum > len(a) / 2:
        print(1)
    else:
        print(0)