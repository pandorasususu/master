#13067. 5202. [파이썬 S/W 문제해결 구현] 3일차 - 화물 도크

tc = int(input())

for _ in range(1, tc+1):
    N = int(input())
    schedule = []
    for t in range(N):
        s, e = map(int, input().split())
        spent = e-s
        schedule.append([e, spent, s])
    # schedule.sort(reverse=True)
    schedule.sort(key = lambda x:(-x[0],x[1]))

    real_schedule = []

    for t1 in range(len(schedule)-1):
        for t2 in range(t1, len(schedule)):
            if schedule[t1][2] < schedule[t2][2]:
                break
        else:
            if real_schedule:
                for t3 in range(len(real_schedule)):
                    if real_schedule[t3][2] < schedule[t1][0]:
                        break
                else:
                    real_schedule.append(schedule[t1])
            else:
                real_schedule.append(schedule[t1])

    # print(real_schedule)
    print(f'#{_} {len(real_schedule)+1}')
'''

3
5
20 23
17 20
23 24
4 14
8 18
10
14 23
2 19
1 22
12 24
21 23
6 15
20 24
1 4
6 15
15 16
15
18 19
2 7
11 15
13 16
23 24
2 14
13 22
20 23
13 19
7 15
5 21
20 24
16 22
17 21
9 24



10
14 23
2 19
1 22
12 24
21 23
6 15
20 24
1 4
6 15
15 16
'''
