# 5251. [파이썬 S/W 문제해결 구현] 7일차 - 최소 이동 거리

tc = int(input())
for _ in range(1, tc+1):
    last_node, path = map(int, input().split())
    inf = 10 ** 6
    arr = [list(map(int, input().split())) for _2 in range(path)]
    adj = [[inf] * (last_node+1) for _3 in range(last_node+1)]
    for i in range(len(arr)):
        r, c, w = arr[i][0], arr[i][1], arr[i][2]
        adj[r][c] = w

    least_path = [0] + [inf] * (last_node)
    for r in range(last_node+1):
        for c in range(last_node+1):
            if least_path[r] + adj[r][c] < least_path[c]:
                least_path[c] = adj[r][c] + least_path[r]
    print(f'#{_} {least_path[-1]}')

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