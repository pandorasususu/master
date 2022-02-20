#백준1913<달팽이>
#이것보다 훨씬 빠르고 간단하게 할 수 있는 방법을 찾아보자
n = int(input())
q = int(input())
from pprint import pprint

arr = [[0]* n for _ in range(n)]
a_list = list(range(1,n**2+1))[::-1]
new_list = []
di = [1,0,-1,0]
dj = [0,1,0,-1]

for idx in range(len(a_list)):
    i, j, cnt = 0, 0, 0
    if arr[i][j] == 0 and cnt % 4 == 0:
        arr[i][j] = a_list[idx]
        i += di[0]
        j += dj[0]
        if i >= n - 1 or arr[i+1][j] != 0:
            cnt += 1
            continue

    elif arr[i][j] == 0 and cnt % 4 == 1:
        arr[i][j] = a_list[idx]
        i += di[1]
        j += dj[1]
        if j >= n - 1 or arr[i][j+1] != 0:
            cnt += 1
            continue

    elif arr[i][j] == 0 and cnt % 4 == 2:
        arr[i][j] = a_list[idx]
        i += di[2]
        j += dj[2]
        if i >=0 or arr[i-1][j] != 0:
            cnt += 1
            continue

    elif arr[i][j] == 0 and cnt % 4 == 3:
        arr[i][j] = a_list[idx]
        i += di[3]
        j += dj[3]
        if arr[i][j-1] != 0:
            cnt += 1
            continue
pprint(arr)



# cnt = 1
# e = 0
# while n > 0:
#     if cnt == 1:
#         new_list.append(a_list[e:e+n])
#         cnt = 0
#         e += n
#         n -= 1
#     else:
#         new_list.append(a_list[e:e+n])
#         cnt += 1
#         e += n
#
# idx1, idx2 = 0, 0
# for e in range(len(new_list)):
#
#     if e % 4 == 0:
#         for i in range(len(new_list[e])):
#             arr[idx1][idx2] = new_list[e][i]
#             idx1 += di[0]
#             idx2 += dj[0]
#
#     elif e % 4 == 1:
#         idx1 -= 1
#         idx2 += 1
#         for i in range(len(new_list[e])):
#             arr[idx1][idx2] = new_list[e][i]
#             idx1 += di[1]
#             idx2 += dj[1]
#
#     elif e % 4 == 2:
#         idx1 -= 1
#         idx2 -= 1
#         for i in range(len(new_list[e])):
#             arr[idx1][idx2] = new_list[e][i]
#             idx1 += di[2]
#             idx2 += dj[2]
#     else:
#         idx1 += 1
#         idx2 -= 1
#         for i in range(len(new_list[e])):
#             arr[idx1][idx2] = new_list[e][i]
#             idx1 += di[3]
#             idx2 += dj[3]
#         idx1 += 1
#         idx2 += 1
#
#
# for row in range(len(arr)):
#     for col in range(len(arr)):
#         print(arr[row][col],end=' ')
#         if arr[row][col] == q:
#             a = row + 1
#             b = col + 1
#     print()
# print(a, b)


