# a = [5,1,2,6,8,1,2,9,7]
# b = a[:]
#
# def sol(idx):
#     if idx == len(a):
#         return
#     else:
#         minI = idx
#         for j in range(idx, len(a)):
#             if a[minI] > a[j]:
#                 a[minI], a[j] = a[j], a[minI]
#
#         sol(idx+1)
#
# sol(0)
#
# print(a)
# b.sort()
#
# print(a == b)

# a = [-1,3,-9,6,7,-6, 1,5,4,-2]
# n = int(input())
# a = list(map(int ,input().split()))
# sub = [0] * len(a)
#
# def sol(idx):
#     global cnt
#     if idx == len(a):
#         total_sum = 0
#         for i in range(len(a)):
#             if sub[i]:
#                 total_sum += a[i]
#         if total_sum == 0:
#             cnt += 1
#             # for j in range(len(a)):
#             #     if sub[j]:
#             #         print(a[j], end=' ')
#             # else:
#             #     print()
#         return
#     else:
#         sub[idx] = 1
#         sol(idx+1)
#
#         sub[idx] = 0
#         sol(idx+1)
#
# cnt = 0
# sol(0)
# print(cnt)

a = [1,2,3,4,5]
p = [0] * 3
used = [0] * 5
def sol(idx, k, m):
    if idx == k:
        print(p)
    else:
        for i in range(m):
            if not used[i]:
                used[i] = 1
                p[idx] = a[i]
                sol(idx+1, k, m)
                used[i] = 0
sol(0, 3, 5)

