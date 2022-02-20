#SWEA1208<Flatten>

''' 출력값이 미묘하게 2정도씩 달라서 당황했는데, max_dump를 줄이는 과정에서 문제가 있었던 듯.
import sys
sys.stdin = open('0210.txt', 'r')

T = 10

def min_to_max(block):
    max_cnd = block[0]
    for idx_2 in range(len(block) - 1, 0, -1):
        for idx_3 in range(idx_2):
            if block[idx_3] > block[idx_3+1]:
                block[idx_3], block[idx_3+1] = block[idx_3+1], block[idx_3]

def second_least(block):
    for iidx in range(len(block)):
        if block[iidx] == block[iidx+1]:
            continue
        else:
            return iidx

def next_tallest(block):
    for iiidx in range(len(block)-1,0,-1):
        if block[iiidx] < block[iiidx-1]:
            block[iiidx], block[iiidx-1] = block[iiidx-1], block[iiidx]

for idx in range(1, T+1):
    max_dump = int(input())
    block = list(map(int, input().split()))
    min_to_max(block)
    # print(block)
    # print(second_least(block))
    while max_dump > 0:
        sl_idx = second_least(block)
        max_dump -= 1
        block[len(block) - 1] -= 1
        block[sl_idx] += 1
        next_tallest(block)

    print(f'#{idx} {block[len(block)-1] - block[0]}')
'''

#깔끔하게 다시 풀어보기
#굳이 처음에 오름차순으로 정렬할 필요가 없었던 것 같다.

import sys
sys.stdin = open('0210.txt', 'r')

T = 10

for idx in range(1, T+1):
    max_dump = int(input())
    block = list(map(int, input().split()))

    max_num = 0
    min_num = 0

    while max_dump >= 0:
        for e in range(100):
            if block[max_num] < block[e]:
                max_num = e
            if block[min_num] > block[e]:
                min_num = e
        if max_dump == 0:
            print(f'#{idx} {block[max_num]-block[min_num]}', max_dump)
        else:
            block[max_num] -= 1
            block[min_num] += 1
        max_dump -= 1
