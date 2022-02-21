#SWEA4837<부분집합의 합>

T = int(input())
M = [i for i in range(1,13)]
mm = len(M)

for _ in range(1, T+1):
    N, K = map(int, input().split())
    ans = 0
    for i in range(1<<mm):
        cnt = 0
        t_sum = 0
        for j in range(mm):
            if i & (1<<j):
                t_sum += M[j]
                cnt += 1
        else:
            if t_sum == K and cnt == N:
                ans += 1
    print(f'#{_}', ans)

