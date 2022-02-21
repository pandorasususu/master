#SWEA13428<숫자 조작>

T = int(input())
for _ in range(1, T+1):
    n = int(input())
    m = n
    arr = [i for i in str(n)]

    for j in range(len(arr)):
        for k in range(len(arr)-1,j,-1):
            

    # min_num = min(arr)
    # max_num = max(arr)
    #
    # for e in range(len(arr)):
    #     if arr[e] == max_num:
    #         max_num = max(arr.remove(max_num))
    #     else:
    #         arr[e], arr[arr.index(max_num)] = arr[arr.index(max_num)], arr[e]
    #         print(*arr)
    #
    #
    #     elif arr[e] == min_num and min_num != 0:
    #         min_num = min(arr.remove(min_num))
    #     else:
    #         arr[e], arr[arr.index(min_num)] = arr[arr.index(min_num)], arr[e]
    #         print(*arr)


    #
    # for j in range(len(arr)):
    #     for k in range(len(arr)-1, j, -1):
''' 
4
12345
54321
142857
10000
'''




