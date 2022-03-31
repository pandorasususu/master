# 5688. 세제곱근을 찾아라
tc = int(input())


def power(a, n):
    if n == 0:
        return 1

    x = power(a, n // 2)

    if n % 2 == 0:
        return x * x

    else:
        return x * x * a

# def solve(n, d):
#     global ans
#     if n % d == 0 and n // d == d * d:
#         ans = d
#         return
#     else:
#         return solve(n, d+1)

for _ in range(1, tc+1):
    n = int(input())
    len_n = len(str(n)) // 3 + 1
    ans = -1
    d = 2
    # end = 10**len_n + 1
    # start = end // 10
    # for i in range(start, end):
    #     if n % i == 0 and n // i == i * i:
    #         # test = n // i
    #         # if test == i * i:
    #         ans = i
    # # solve(n, d)
    power()
    print(f'#{_} {ans}')



    # while True:
    #     if n % d:
    #         d += 1
    #     else:
    #         mlt.append(d)
    #         n //= d
    #         if n == 1:
    #             break
    #
    # triple = []
    # test = set(mlt)
    # print(mlt, test)
    # for e in test:
    #     again = [e] * mlt.count(e)
    #     triple.append(again)
    #
    # result = True
    # final_ans = 1
    #
    # for t in triple:
    #     if len(t) % 3 != 0:
    #         result = False
    #     else:
    #         final_ans *= (t[0] * (len(t) // 3))
    #
    #
    # if result == False:
    #     print(f'#{_} {ans}')
    # else:
    #     print(f'#{_} {final_ans}')

    #zip함수는 넘기는 인자 중 최소 길이를 기준으로 데이터가 엮이므로 zip함수를 쓰는 건 부적절한 것 같다.
    # triple = []
    # if len(set(mlt)) == 1:
    #     if not len(mlt) % 3:
    #         ans = 1
    #         for x in range(len(mlt) // 3):
    #             ans *= mlt[0]
    # else:
    #     test = set(mlt)
    #     for e in test:
    #         again = [e] * mlt.count(e)
    #         triple.append(again)
    #     triple = list(zip(*triple))
    #     triple_sub = triple[0]
    #
    #     if triple == triple_sub * len(triple):
    #         if len(triple) % 3 == 0:
    #             ans = 1
    #             for e in triple_sub:
    #                 ans *= e

    # 아마 답은 맞을텐데 제한시간 초과
    # for i in range(2, n):
    #     if n % i == 0:
    #         mlt.append(i)
    # for m in mlt:
    #     test = n
    #     if n % m == 0:
    #         test //= m
    #         if test == m ** 2:
    #             ans = m



'''


3
27
7777
64

10
3513213351484484
6846513513512222
3843841335135222
1111111115414222
3513513213222122
3213213213205151
3213213213351511
1351351351353511
1351351351335135
1000000000000000
'''