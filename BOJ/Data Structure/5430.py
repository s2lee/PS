import sys
input = sys.stdin.readline

for _ in range(int(input())):
    p_list = list(map(len, input().rstrip().replace('RR', '').split('R')))
    n = int(input())
    n_list = input().rstrip()[1:-1].split(',')

    lo, hi = sum(p_list[::2]), n - sum(p_list[1::2])

    if lo <= hi:
        print_list = n_list[lo:hi] if len(p_list) % 2 else n_list[lo:hi][::-1]
        print('[' + ','.join(print_list) + ']')
    else:
        print('error')
