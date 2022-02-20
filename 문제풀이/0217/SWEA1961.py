#SWEA1961<숫자배열회전>
from pprint import pprint
import sys
sys.stdin = open('1261.txt')
T = int(input())

for _ in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    ans_arr = [[0] * (3*N + 2) for _ in range(N)]
    for r in range(len(arr)):
        ans_arr[r][N] = ' '
        ans_arr[r][len(ans_arr[r])-N-1] = ' '

    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    cnt = 0
    a, b = 0, N - 1
    while True:
        if cnt == 3: #3
            break
        if cnt == 0:
            for idx in range(len(arr)):
                for e in range(len(arr[idx])):
                    ans_arr[a][b] = arr[idx][e]
                    a += 1
                b -= 1
                a = 0
        else: #cnt=1 a=0 b=(N-1)+(N+1) #cnt=2 a=0 b=(N-1)+2(N+1)
            s = b-2*N
            end = b-N
            for idx in range(N):
                for e in range(s, end):
                    ans_arr[a][b] = ans_arr[idx][e]
                    a += 1
                b -= 1
                a = 0

        cnt += 1
        b = (N-1) + (N+1) * cnt


    print(f'#{_}')
    for row in ans_arr:
        for i in row:
            print(i,end='')
        print()
