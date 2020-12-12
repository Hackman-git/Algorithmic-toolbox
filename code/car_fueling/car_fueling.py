# python3
import sys


def compute_min_refills(distance, tank, stops):
    num_refills = 0
    current = 1
    last_refill_pt = 0
    used = 0
    stops.insert(0,0)

    while current != (len(stops)):
        if (stops[current] - stops[last_refill_pt]) <= tank:
            used = stops[current] - stops[last_refill_pt]
            current += 1
            if(current == len(stops)):
                if distance - stops[last_refill_pt] > tank:
                    last_refill_pt = current - 1
                    num_refills += 1
                    if distance - stops[last_refill_pt] > tank:
                        return -1
        

        else:
            if ((stops[current] - stops[current-1]) > tank):
                return -1
            else:
                num_refills += 1
                last_refill_pt = current - 1
                current += 1
                if(current == len(stops)):
                    if distance - stops[last_refill_pt] > tank:
                        last_refill_pt = current - 1
                        num_refills += 1
                        if distance - stops[last_refill_pt] > tank:
                            return -1
            
        
    return num_refills

if __name__ == '__main__':
    a = []
    for i in range(3):
        x = int(input())
        a.append(x)
    d = a[0]
    m = a[1]
    stops = list(map(int, input().split()))
    print(compute_min_refills(d, m, stops))