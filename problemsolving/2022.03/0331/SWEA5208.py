# 13125. 5208. [파이썬 S/W 문제해결 구현] 5일차 - 전기버스2
# 왜 minV-1 해야 답이 나오는지 명확히 분석하기
# 2022.04.02 왜냐하면 출발하는 첫번째 정류장에서도 change+1을 했기 때문
# sol 함수 내부 반복문에서 경우를 나눠 처리하느니, 마지막에 -1해주는 게 편해서 수정하지 않음

tc = int(input())

def sol(idx, change, path):
    global minV
    if idx >= N - 1:
        if minV > change:
            minV = change
            return
        return
    else:
        # 1에서 해당 정류장의 충전지+1 만큼 도는 이유는, 충전 시 갈 수 있는 모든 거리에 대해서 순회하기 위함
        # 예를 들어 충전지가 3이라고 하면, 1/2/3 만큼 떨어진 정류장을 갈 수 있으므로 해당 경우 모두를 순회하기 위함
        for b in range(1, station_battery[idx]+1):
            idx += b
            change += 1
            if change > minV:
                return
            sol(idx, change, path + [idx])
            idx -= b
            change -= 1

for _ in range(1, tc+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    station_battery = arr[1:]
    minV = N
    path = []
    sol(0, 0, path)

    print(f'#{_} {minV- 1}')
