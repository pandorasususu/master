#SWEA1974<스도쿠 검정>

import sys
sys.stdin = open('1974.txt')

def row_check(arr):
    for row in range(9):
        row_sum = 0
        for col in range(9):
            row_sum += arr[row][col]
        if row_sum != 45:
            return 0
        else:
            continue
    else:
        return 1


T = int(input())

for _ in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = 1

    result1 = row_check(arr)
    if result1 == 0:
        print(f'#{_} {result1}')
        continue

    result2 = row_check(list(zip(*arr)))
    if result2 == 0:
        print(f'#{_} {result2}')
        continue

    for row in [0,3,6]:
        for col in [0,3,6]:
            block_sum = 0
            for r_dir in range(3):
                for c_dir in range(3):
                    block_sum += arr[row+r_dir][col+c_dir]
            if block_sum != 45:
                result = 0
                break
        if result == 0:
            break

    print(f'#{_} {result}')


