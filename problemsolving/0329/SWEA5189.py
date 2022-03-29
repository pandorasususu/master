# 5189. [파이썬 S/W 문제해결 구현] 2일차 - 전자카트

tc = int(input())

def sol(idx):
    if idx >= N:
        battery = 0
        for v in range(len(path)-1):
            start = path[v]
            end = path[v+1]
            battery += arr[start][end]
        num_cnd.append(battery)

    else:
        for i in range(1, N):
            if not visited[i]:
                path[idx] = office[i]
                visited[i] = 1
                sol(idx+1)
                visited[i] = 0


for _ in range(1,tc+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    office = [i for i in range(N)] 
    path = [0] * (N+1)
    visited = [0] * N
    num_cnd = []
    sol(1)
    print(f'#{_} {min(num_cnd)}')
