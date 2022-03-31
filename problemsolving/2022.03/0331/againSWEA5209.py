# 5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용
#실행속도가 좀 느린 거 같은데
tc = int(input())

def sol(idx, cost):
    global min_cost
    if idx >= N:
        if cost < min_cost:
            min_cost = cost
    else:
        for idx_f in range(N):
            if factory[idx_f] not in perm:
                perm.append(factory[idx_f])
                cost += arr[idx][idx_f]
                if cost > min_cost:
                    cost -= arr[idx][idx_f]
                    perm.pop(idx)
                    continue
                else:
                    sol(idx+1, cost)
                    cost -= arr[idx][idx_f]
                    perm.pop(idx)

for _ in range(1, tc+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    factory = [i for i in range(N)]
    min_cost = 10 ** 10
    perm = []
    sol(0, 0)

    print(f'#{_} {min_cost}')

'''

1
3
73 21 21
11 59 40
24 31 83

3
3
73 21 21
11 59 40
24 31 83
5
93 4 65 31 66
63 12 60 60 84
87 57 44 35 20
12 9 40 12 40
60 21 3 49 54
6
55 83 32 79 53 70
77 88 80 93 42 29
54 26 5 10 25 94
77 92 82 83 11 51
84 11 21 62 45 58
37 88 13 34 41 4
'''