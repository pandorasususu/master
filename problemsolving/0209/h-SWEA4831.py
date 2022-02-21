# SWEA4831<전기버스>
'''
T = int(input())
for _ in range(1, T + 1):
    K, N, M = map(int, input().split())
    bus_station = list(map(int, input().split()))

    # 출발점과 종착점 추가
    bus_station.insert(0, 0)
    bus_station.insert(len(bus_station), N)

    stop = 0  # 멈춘 횟수
    fuel = K  # 한번 충전으로 갈 수 있는 거리이며 최대 연료치를 뜻함

    for idx in range(len(bus_station) - 1):
        if idx == 0:  # 출발할 때는 완전히 충전되었으므로 반복문 다시 돌림.
            continue
        fuel -= (bus_station[idx] - bus_station[idx - 1])  # 주행거리만큼 감소된 연료

        if (bus_station[idx + 1] - bus_station[idx] > K):  # 충전을 해도 다음 정류장에 도착하지 못할 때 0출력하고 반복 중단
            print(f'#{_} 0')
            break

        # 이번 정류장에 도착했을 때 다음정류장 까지 갈 수 있는 연료가 남아있으면 멈추지 않음
        elif (bus_station[idx + 1] - bus_station[idx] <= fuel):
            if idx == len(bus_station) - 2:  # 마지막 정류장에 도착하고, 종착점까지 갈 수 있다면 지금까지 멈춘 횟수 출력
                print(f'#{_} {stop}')

        # 이번 정류장에 도착했을 때 다음정류장 까지 갈 수 있는 연료가 남아있지 않으면 멈춘 횟수를 더하고 연료를 충전
        elif (bus_station[idx + 1] - bus_station[idx] > fuel):
            if idx == len(bus_station) - 2:  # 마지막 정류장에 도착하면 지금까지 멈춘 횟수 출력
                stop += 1
                print(f'#{_} {stop}')
            else:
                stop += 1
                fuel = K
'''

#0210 다시 풀어보기
#position 움직이기
#현재 위치에서 가장 멀리 있는 정류장을 찾는 풀이
''' 
T = int(input())
for _ in range(1, T + 1):
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))
    position = 0
    stop = 0
    while True:
        stop_sign = False
        position += K
        if position >= N:
            break
        else: #현재 갈 수 있는 정류장 중 가장 멀리 떨어져 있는 정류장 찾기
            for idx in range(position, position-K, -1):
                for s in station:
                    if idx == s:
                        position = idx
                        stop += 1
                        stop_sign = True
                        break
                if stop_sign == True:
                    break
            else:
                stop = 0
                break
    print(f'#{_}', stop)
'''