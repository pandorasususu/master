# 5201. [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반

tc = int(input())

for _ in range(1, tc+1):
    cnt_num, trk_num = map(int, input().split())
    cnt_w = list(map(int, input().split()))
    trk_mw = list(map(int, input().split()))
    result = 0

    cnt_w.sort(reverse=True)
    trk_mw.sort(reverse=True)

    ans = 0
    t = 0
    for c in range(len(cnt_w)):
        if cnt_w[c] <= trk_mw[t]:
            ans += cnt_w[c]
            t += 1
            if t >= trk_num:
                break
        else:
            continue
    print(f'#{_} {ans}')
'''

3
3 2
1 5 3
8 3
5 10
2 12 13 11 18
17 4 7 20 3 9 7 9 20 5
10 12
10 13 14 6 19 11 5 20 11 14
5 18 17 8 9 17 18 4 1 16 15 13
'''



