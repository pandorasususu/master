#SWEA1244<최대 상금>
import sys
sys.stdin = open('1244.txt')
T = int(input())

for _ in range(1, 6):
    a, b = map(int, input().split())
    ans = []
    for i in range(len(str(a))):
        ans.append(str(a)[i])
    ans = list(map(int, ans))

    # for i in range(b):
    #     for e in range(len(ans)):
    #         for ee in range(len(ans) - 1, e, -1):
    #             ans2 = ans[:]
    #             ans2[e], ans2[ee] = ans2[ee], ans2[e]



    cmp = []
    def shuffle(ans, b):
        if b == 0:
            cmp.append(ans)
        else:
            for e in range(len(ans)):
                for ee in range(len(ans) - 1, e, -1):
                    ans2 = ans[:]
                    ans2[e], ans2[ee] = ans2[ee], ans2[e]

                    for e2 in range(len(ans2)):
                        for ee2 in range(len(ans) - 1, e, -1):
                            ans2 = ans[:]
                            ans2[e], ans2[ee] = ans2[ee], ans2[e]
    shuffle(ans, b)
    print(f'#{_}',end=' ')
    for i in max(cmp):
        print(i, end='')
    # while b > 0:
    #     for e in range(len(ans)):
    #         for ee in range(len(ans)-1, e, -1):
    #             ans2 = ans[:]
    #             ans2[e], ans2[ee] = ans2[ee], ans2[e]
    #             ans2 = map(str, ans2)
    #             cmp.append(''.join(ans2))
    #     b -= 1
    # cmp = list(map(int, cmp))
    # print(len(cmp), max(cmp))

    '''
    input
    10
    123 1 #3
    2737 1 #6
    757148 1 #15
    78466 2 #20 ?100
    32888 2 #20 ?100
    777770 5 #75 ?15^5
    436659 2 #30 ?15^2
    431159 7 #105 ?15^7
    112233 3 #45 ?15^3
    456789 10 #150 ?15*10

    ans
    #1 321
    #2 7732
    #3 857147
    #4 87664
    #5 88832
    #6 777770
    #7 966354
    #8 954311
    #9 332211
    #10 987645
    '''

    # ans2 = ans[:]
    # # ans2 = [ii for ii in ans]
    # la = len(ans)
    # for j in range(la):
    #     for k in range(la-1, j, -1):
    #         if ans2[j] < ans2[k]:
    #             ans2[j], ans2[k] = ans2[k], ans2[j]
    # ans = list(map(int, ans))
    # ans2 = list(map(int, ans2))
    #
    # stop = False
    # while ans != ans2:
    #     for e in range(la):
    #         if ans[e] != ans2[e]:
    #             idx = []
    #             for ee in range(la):
    #                 if ans[ee] == ans2[e]:
    #                     idx.append(ee)
    #             # print(idx,max(idx))
    #             ans[e], ans[max(idx)] = ans[max(idx)], ans[e]
    #             # print(ans)
    #             b -= 1
    #             if b == 0:
    #                 stop = True
    #         if stop == True:
    #             break
    #     if stop == True:
    #         break
    # print(f'#{_}',end=' ')
    # for final in ans:
    #     print(final,end='')
    # print()
'''
input
10
123 1 #3
2737 1 #4
757148 1 #6
78466 2 #10
32888 2 #10
777770 5 #6
436659 2 #15
431159 7 #
112233 3 #20
456789 10 #

ans
#1 321
#2 7732
#3 857147
#4 87664
#5 88832
#6 777770
#7 966354
#8 954311
#9 332211
#10 987645
'''