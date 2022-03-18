#SWEA6485 그렇게 어려운 문제는 아니라고 생각했는데, 고려해야 하는 조건들이 좀 있었다.
#다시 풀어보기
# T = int(input())
#
#
# for idx in range(1, T+1):
#     N = int(input())
#     bus_path = []
#     for _ in range(N):
#         s, e = map(int, input().split())
#         bus = list(range(s, e+1))
#         bus_path.append(bus)
#
#     P = int(input())
#
#     total_station = [0] * 5000
#
#     for bus_drive in bus_path:
#         for station in bus_drive:
#             total_station[station-1] += 1
#
#     final_ans = []
#     for _ in range(P):
#         bus_station = int(input())
#         final_ans.append(total_station[bus_station-1])
#
#     print(f'#{idx}', *final_ans)


################################
#SWEA 6485
#다시 풀어보기 5천개의 버스정류장 고려
#마지막에 ans=[]만들지 않고 바로 print하고 싶었지만 어째서인지 계속 fail되므로 ans=[]를 만들 수 밖에 없었다.
'''
T = int(input())

for idx in range(1, T + 1):
    N = int(input())
    total_station = [0] * 5000

    for _ in range(N):
        s, e = map(int, input().split())
        for stop in range(s-1, e):
            total_station[stop] += 1

    P = int(input())
    ans =[]
    for _ in range(P):
        station = int(input())
        ans.append(total_station[station-1])

    print(f'#{idx}', *ans)
'''