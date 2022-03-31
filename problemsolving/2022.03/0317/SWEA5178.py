# 5178. [파이썬 S/W 문제해결 기본] 8일차 - 노드의 합

tc = int(input())

for _ in range(1, tc+1):
    N, M, L = map(int, input().split())
    arr = [list(map(int, input().split())) for m in range(M)]

    # 완전 이진 트리 만들기
    parent = [i for i in range(N+1)]
    c1 = [0] * (N+1)
    c2 = [0] * (N+1)
    idx = 1
    while True:
        if c1[idx] == 0:
            c1[idx] = 2*idx
            if 2*idx == N:
                break
            c2[idx] = 2*idx + 1
            if 2*idx + 1 == N:
                break
        idx += 1


    value = [0] * (N+1)

    for mm in range(M):
        value[arr[mm][0]] = arr[mm][1]

    idx2 = N
    while True:
        if idx2 == 1:
            break
        if idx2 % 2:
            value[idx2 // 2] = value[idx2] + value[idx2 - 1]
            idx2 -= 2

        else:
            value[idx2 // 2] = value[idx2]
            idx2 -= 1


    print(f'#{_} {value[L]}')


'''
3
5 3 2
4 1
5 2
3 3
10 5 2
8 42
9 468
10 335
6 501
7 170
17 9 4
16 479
17 359
9 963
10 465
11 706
12 146
13 282
14 828
15 962
'''