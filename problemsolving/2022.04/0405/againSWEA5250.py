# 5250. [파이썬 S/W 문제해결 구현] 7일차 - 최소 비용

def sol(sr, sc, fuel):
    global min_fuel
    if fuel_spent[sr][sc] > min_fuel:
        return
    if sr == n - 1 and sc == n - 1:
        if fuel_spent[sr][sc] < min_fuel:
            min_fuel = fuel_spent[sr][sc]

    while q:
        cr, cc = q.pop(0)
        for dr, dc in [[1,0],[-1,0],[0,1],[0,-1]]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < n and 0 <= nc < n:
                if arr[nr][nc] > arr[cr][cc]:
                    fuel += 1 + arr[nr][nc] - arr[cr][cc]
                    if fuel > min_fuel:
                        return
                    else:
                        fuel_spent[nr][nc] = fuel
                        sol(nr, nc, fuel)
                        fuel -= 1 + arr[nr][nc] - arr[cr][cc]
                else:
                    fuel += 1
                    if fuel > min_fuel:
                        return
                    else:
                        fuel_spent[nr][nc] = fuel
                        sol(nr, nc, fuel)
                        fuel -= 1



tc = int(input())
for _ in range(1, tc+1):
    n = int(input())
    inf = 10**6
    arr = [list(map(int, input().split())) for _2 in range(n)]
    fuel_spent = [[inf] * n for _ in range(n)]
    q = [[0,0]]
    min_fuel = 10 ** 10
    sol(0,0,0)
    print(f'#{_} {min_fuel}')

'''
3
3
0 2 1
0 1 1
1 1 1
5
0 0 0 0 0
0 1 2 3 0
0 2 3 4 0
0 3 4 5 0
0 0 0 0 0
5
0 1 1 1 0
1 1 0 1 0
0 1 0 1 0
1 0 0 1 1
1 1 1 1 1
'''