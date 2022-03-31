# 13125. 5208. [파이썬 S/W 문제해결 구현] 5일차 - 전기버스2
# 왜 minV-1 해야 답이 나오는지 명확히 분석하기

tc = int(input())

def sol(idx, change):
    global minV
    if idx >= N - 1:
        if minV > change:
            minV = change
        return
    else:
        for b in range(1, station_battery[idx]+1):
            idx += b
            change += 1
            if change > minV:
                return
            sol(idx, change)
            idx -= b
            change -= 1

for _ in range(1, tc+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    station_battery = arr[1:]
    minV = N
    sol(0, 0)

    print(f'#{_} {minV- 1}')
'''

3
5 2 3 1 1
10 2 1 3 2 2 5 4 2 1
10 1 1 2 1 2 2 1 2 1
'''