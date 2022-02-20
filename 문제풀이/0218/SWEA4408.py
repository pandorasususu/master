#SWEA4408<자기 방으로 돌아가기>
T = int(input())

for _ in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    corridor = [0] * 200

    max_time = 0
    for r in range(len(arr)):
        for i in range(2):
            if arr[r][i] % 2 == 0:
                arr[r][i] -= 1
            arr[r][i] //= 2

        if arr[r][0] > arr[r][1]:
            start, end = arr[r][1], arr[r][0]
        else:
            start, end = arr[r][0], arr[r][1]

        for j in range(start, end+1): #방에 도착하기 위해 지나가야하는 경로를 표시, corridor의 각 요소는 해당 위치를 지나간 사람의 수를 뜻함
            corridor[j] += 1
            if corridor[j] > corridor[max_time]:
                max_time = j

    print(F"#{_} {corridor[max_time]}")

'''
1
5
1 20
2 100
4 16
50 300
15 30
'''




