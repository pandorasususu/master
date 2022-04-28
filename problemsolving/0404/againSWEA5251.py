# 13177. 5251. [파이썬 S/W 문제해결 구현] 7일차 - 최소 이동 거리

tc = int(input())
for _ in range(1, tc+1):
    last_node, rd = map(int, input().split())
    min_path = [0] + [10**10] * last_node
    adj = [[0] * (last_node + 1) for _ in range(last_node + 1)]
    for i in range(rd):
        start, end, weight = map(int, input().split())
        adj[start][end] = weight
    for r in range(last_node+1):
        minV = 10**10
        for c in range(last_node+1):
            if adj[r][c] != 0 and adj[r][c] < minV:
                minV = adj[r][c]
                next_node = c
        if min_path[r] + minV < min_path[next_node]:
            min_path[next_node] = min_path[r] + minV
    print(f'#{_} {min_path[last_node]}')


'''
1
2 3
0 1 1
0 2 6
1 2 1

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