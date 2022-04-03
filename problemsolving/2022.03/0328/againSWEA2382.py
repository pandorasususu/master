#SWEA2382 미생물격리

# tc = int(input())
# di, dj = (0, -1, 1, 0, 0), (0, 0, 0, -1, 1)
# opp = [0,2,1,4,3]
# for _ in range(1, tc+1):
#     N, M, K = map(int, input().split())
#     arr = [list(map(int, input().split())) for _1 in range(K)]
#
#
#     for _2 in range(M):
#         for i in range(len(arr)):
#             arr[i][0] = arr[i][0] + di[arr[i][3]]
#             arr[i][1] = arr[i][1] + dj[arr[i][3]]
#             if arr[i][0] == 0 or arr[i][0] == N - 1 or arr[i][1] == 0 or arr[i][1] == N-1:
#                 arr[i][2] //= 2
#                 arr[i][3] = opp[arr[i][3]]
#
#         arr.sort(key=lambda x: (x[0],x[1], x[2]), reverse=True)
#
#         i = 1
#         while i < len(arr):
#             if arr[i-1][0] == arr[i][0] and arr[i-1][1] == arr[i][1]:
#                 arr[i-1][2] += arr[i][2]
#                 arr.pop(i)
#             else:
#                 i += 1
#     ans = 0
#     for i in range(len(arr)):
#         ans += arr[i][2]
#
#     print(f'#{_} {ans}')

from pprint import pprint

import sys
sys.stdin = open('micro.txt')

tc = int(input())
dr, dc = [0,-1,1,0,0],[0,0,0,-1,1]
opp = [0,2,1,4,3]

for _ in range(1, tc+1):
    size, time, groups = map(int, input().split())
    micro = [list(map(int, input().split())) for _1 in range(groups)]

    for _2 in range(time):
        for idx_g in range(len(micro)):
            r, c, num, move = micro[idx_g][0], micro[idx_g][1], micro[idx_g][2], micro[idx_g][3]
            print(micro[idx_g])
            micro[idx_g][0] += dr[move]
            micro[idx_g][1] += dc[move]
            if micro[idx_g][0] == 0 or micro[idx_g][0] == size-1 or micro[idx_g][1] == 0 or micro[idx_g][1] == size-1:
                micro[idx_g][2] //= 2
                micro[idx_g][3] = opp[micro[idx_g][3]]

        micro.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)

        idx_f = 1
        while idx_f < len(micro):
            if micro[idx_f-1][0] == micro[idx_f][0] and micro[idx_f-1][1] == micro[idx_f][1]:
                micro[idx_f-1][2] += micro[idx_f][2]
                micro.pop(idx_f)
            else:
                idx_f += 1
    cnt = 0
    for idx_m in range(len(micro)):
        cnt += micro[idx_m][2]

    print(f'#{_} {cnt}')
