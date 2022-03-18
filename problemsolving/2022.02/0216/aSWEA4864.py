#SWEA4864<문자열 비교>
#왜 시간초과가 나지 않았을까, for문 대신 while문을 쓴 것 뿐인데.
T = int(input())
for _ in range(1, T+1):
    inner = list(input())
    total = list(input())
    break_p = False
    i = -1
    while True:
        i += 1
        if i >= len(total)-1:
            print(f'#{_} 0')
            break
        if break_p == True:
            break

        if total[i] == inner[0]:
            ii = i
            for j in range(len(inner)):
                if total[ii] == inner[j]:
                    ii += 1
                else:
                    i += j
                    break
            else:
                print(f'#{_} 1')
                break_p = True





        # if total[i] in inner:
        #     ii = i
        #     for j in range(len(inner)):
        #         if total[ii] == inner[j]:
        #             ii += 1
        #             cnt += 1
        #         if cnt == len(inner):
        #             break_p = True
        # if break_p == True:
        #     print(f'#{_} 1')
        #     break



    # i = 0
    # break_p = False
    # while True:
    #     for k in range(len_i-1, -1, -1):
    #         if total[i + len_i -1] == inner[k]:
    #             for l in range((i + len_i -1) - k, (i + len_i -1) + (len_i - k) +1):
    #                 for aa in range(len_i):
    #                     if total[l] != inner[aa]:
    #                         i += len_i
    #                         break_p = True
    #                         break
    #                 else:
    #                     print(f'#{_} 1')
    #                     break_p = True
    #                     break
    #     if break_p == True:
    #         break
    #
    #     if i >= len(total):
    #         print(f'#{_} ')
    #         break

'''
000X0
abcd

'''

