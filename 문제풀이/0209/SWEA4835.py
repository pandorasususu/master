# #SWEA4835<구간합>
''' 간단하게 접근해서 빨리 푸는 게 최고. 순서대로 생각해보자.
T = int(input())

for _ in range(1, T+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))

    m = M // 2
    start = 0
    for e in num_list[:M]:
        start += e
    start2 = start

    for idx in range(len(num_list)-M+1):
        compare = 0
        for ee in num_list[idx:idx+M]:
            compare += ee
        if start < compare:
            start = compare


    for idx in range(len(num_list)-M+1):
        compare = 0
        for ee in num_list[idx:idx+M]:
            compare += ee
        if start2 > compare:
            start2 = compare
    print(f'#{_} {start-start2}')
'''