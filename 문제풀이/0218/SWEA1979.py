#SWEA1979<어디에 단어가 들어갈 수 있을까>
import sys
sys.stdin = open('1979.txt')
def check(arr):
    cnt = 0
    for r in range(N):
        mark = 0
        for c in range(N):
            if arr[r][c] == 1:
                mark += 1
                if mark == K:
                    if c == N - 1 or arr[r][c + 1] != 1:
                        mark = 0
                        cnt += 1
            else:
                mark = 0
    return cnt

T = int(input())
for _ in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result1 = check(arr)
    result2 = check(list(zip(*arr)))
    print(f'#{_} {result1+result2}')