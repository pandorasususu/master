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


#live answer
'''
def DFS(n, ssum):
    global ans
     
    if ssum >= B+ans:
        return
     
    if n==N:
        if ssum >= B and ans > ssum-B:
            ans = ssum-B
        return
 
    DFS(n+1, ssum+lst[n]) # 포함하는 경우
    DFS(n+1, ssum)  # 포함하지 않는 경우
 
 
T = int(input())
# T = 10
for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = 12345678
    DFS(0, 0)
    print(f'#{test_case} {ans}')
'''