# 13177. 5251. [파이썬 S/W 문제해결 구현] 7일차 - 최소 이동 거리

tc = int(input())

def sol(start, ans):
    global min_length
    for idx in range(N+1):
        if adj[start][idx]:
            ans += adj[start][idx]
            if idx != N:
                sol(idx, ans)
                ans -= adj[start][idx]

            else:
                if ans < min_length:
                    min_length = ans
    else:
        return

for _ in range(1,tc+1):
    N, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]

    adj = [[0] * (N+1) for _ in range(N+1)]

    for idx in range(len(arr)):
        adj[arr[idx][0]][arr[idx][1]] = arr[idx][2]

    min_length = 10**10
    sol(0,0)

    print(f'#{_} {min_length}')
'''
3
2 3
0 1 1
0 2 6
1 2 1
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10
'''