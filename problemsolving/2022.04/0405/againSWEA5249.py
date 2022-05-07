# 5249. [파이썬 S/W 문제해결 구현] 7일차 - 최소 신장 트리

def union(a, b):
    p_a = find_set(a)
    p_b = find_set(b)
    parent_node[p_b] = p_a

def find_set(x):
    if parent_node[x] == x:
        return x
    else:
        return find_set(parent_node[x])

tc = int(input())
for _ in range(1, tc+1):
    last_node, road = map(int, input().split())
    inf = 10 ** 6
    arr = [list(map(int, input().split())) for _2 in range(road)]

    parent_node = [i for i in range(last_node+1)]
    arr.sort(key = lambda x: x[2])
    ans = 0
    path = [0]

    for i in range(road):
        if find_set(arr[i][0]) == find_set(arr[i][1]):
            continue
        ans += arr[i][2]
        path.append(arr[i][1])
        union(arr[i][0], arr[i][1])

    print(f'#{_} {ans}')

'''
3
2 3
0 1 1
0 2 1
1 2 6
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

