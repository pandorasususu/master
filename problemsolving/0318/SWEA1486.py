# 1486. 장훈이의 높은 선반

tc = int(input())

def solve(idx):
    if idx == N:
        cnd = 0
        for i in range(N):
            if pick[i]:
                cnd += height[i]
        if cnd >= B:
            cnd_height.append(abs(cnd-B))
        return
    else:
        pick[idx] = 1
        solve(idx+1)

        pick[idx] = 0
        solve(idx+1)

for _ in range(1, tc+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    pick = [0] * N
    cnd_height = []
    solve(0)
    print(f'#{_} {min(cnd_height)}')
