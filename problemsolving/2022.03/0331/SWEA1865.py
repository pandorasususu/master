# 1865. 동철이의 일 분배

tc = int(input())

def sol(idx, prb):
    global max_prb
    if idx >= N:
        if prb > max_prb:
            max_prb = prb
        return
    else:
        for idx_e in range(N):
            if employee[idx_e] not in perm:
                if arr[idx][employee[idx_e]] == 0:
                    continue
                prb *= arr[idx][employee[idx_e]]
                if prb < max_prb:
                    prb /= arr[idx][employee[idx_e]]
                    continue
                perm.append(employee[idx_e])
                sol(idx + 1, prb)
                prb /= arr[idx][employee[idx_e]]
                perm.pop(idx)
        # for idx_p in range(N):
        #     if not used[idx_p]:
        #         if arr[idx][employee[idx_p]] == 0 or prb < max_prb:
        #
        #         perm[idx] = employee[idx_p]
        #         used[idx_p] = 1
        #
        #         sol(idx+1, prb)
        #         used[idx_p] = 0


        # for idx_e in range(N):
        #     if employee[idx_e] not in perm:
        #         if arr[idx][employee[idx_e]] == 0:
        #             continue
        #         prb *= arr[idx][employee[idx_e]]
        #         if prb < max_prb:
        #             prb /= arr[idx][employee[idx_e]]
        #             continue
        #         perm.append(employee[idx_e])
        #         sol(idx + 1, prb)
        #         prb /= arr[idx][employee[idx_e]]
        #         perm.pop(idx)



for _ in range(1, tc+1):
    N = int(input())
    employee = [i for i in range(N)]
    arr = list(list(map(lambda x : float(x) / 100, input().split())) for _ in range(N))
    perm = [0] * N
    max_prb = -1
    used = [0] * N
    sol(0, 1)

    print(f'#{_} {round(max_prb*100, 6):6f}')


'''
1
3
13 0 50
12 70 90
25 60 100

1
15
6 82 3 49 62 7 6 24 71 22 44 86 92 30 87
74 57 96 30 5 93 64 46 42 35 65 81 9 84 50
66 50 51 74 90 94 22 46 10 14 2 100 61 97 19
95 37 82 57 35 41 72 1 81 27 92 60 73 89 83
51 31 77 66 27 48 23 0 11 72 42 56 54 11 51
78 37 34 40 14 5 40 75 11 20 33 87 37 14 19
39 17 95 19 76 87 1 52 27 53 71 11 13 65 84
8 23 98 29 42 21 42 88 40 49 51 36 77 85 30
65 56 97 70 82 35 91 92 100 94 36 50 43 93 46
35 88 9 57 32 69 100 62 91 57 52 45 34 98 79
76 91 91 2 34 89 97 77 80 61 73 10 95 52 87
84 11 33 31 37 56 4 72 12 89 71 64 23 24 56
30 1 53 71 72 58 14 44 4 0 7 56 19 62 98
92 21 3 81 70 32 76 36 97 46 18 99 39 39 42
41 15 81 21 32 69 96 55 58 34 77 0 79 39 48

3
4
71 51 30 1
29 63 32 93
84 94 33 21
56 40 80 31
15
6 82 3 49 62 7 6 24 71 22 44 86 92 30 87
74 57 96 30 5 93 64 46 42 35 65 81 9 84 50
66 50 51 74 90 94 22 46 10 14 2 100 61 97 19
95 37 82 57 35 41 72 1 81 27 92 60 73 89 83
51 31 77 66 27 48 23 0 11 72 42 56 54 11 51
78 37 34 40 14 5 40 75 11 20 33 87 37 14 19
39 17 95 19 76 87 1 52 27 53 71 11 13 65 84
8 23 98 29 42 21 42 88 40 49 51 36 77 85 30
65 56 97 70 82 35 91 92 100 94 36 50 43 93 46
35 88 9 57 32 69 100 62 91 57 52 45 34 98 79
76 91 91 2 34 89 97 77 80 61 73 10 95 52 87
84 11 33 31 37 56 4 72 12 89 71 64 23 24 56
30 1 53 71 72 58 14 44 4 0 7 56 19 62 98
92 21 3 81 70 32 76 36 97 46 18 99 39 39 42
41 15 81 21 32 69 96 55 58 34 77 0 79 39 48
1
32
'''