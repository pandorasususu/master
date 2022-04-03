#13173. 5247. [파이썬 S/W 문제해결 구현] 6일차 - 연산

func = [lambda x: x+1, lambda x: x-1, lambda x: x*2, lambda x: x-10]

tc = int(input())

for _ in range(1, tc+1):
    start, end = map(int, input().split())
    cnt, stack, found, checked = 0, [start], False, [True] * 1000001

    while stack:
        cnt += 1
        nums = {}
        for start in stack:
            for f in func:
                c_num = f(start)
                if c_num > 10 ** 6 or c_num < 1:
                    continue
                elif c_num == end:
                    found = True
                    break
                else:
                    if nums.get(c_num) is None and checked[c_num]:
                        checked[c_num] = False
                        nums[c_num] = True
        if found:
            break
        else:
            stack = list(nums.keys())
    print(f'#{_} {cnt}')

# def sol(N, M, cnt):
#     global minV
#     if N == M:
#         if minV > cnt:
#             minV = cnt
#             return
#         return
#
#     else:
#         if cnt >= minV or N > 10 ** 6:
#             return
#         sol(N + 1, M, cnt + 1)
#         sol(N * 2, M, cnt + 1)
#         if N > 1:
#             sol(N - 1, M, cnt + 1)
#         if N > 10:
#             sol(N - 10, M, cnt + 1)
#
# tc = int(input())
#
# for _ in range(1, tc+1):
#     N, M = map(int, input().split())
#     # s, e = N, M
#     cnt = 0
#     minV = 10 ** 10
#     sol(N, M, cnt)
#
#     print(f'#{_} {minV}')
'''
1
36 100


3
2 7
3 15
2 200


3
2 7
3 15
36 1007
'''
