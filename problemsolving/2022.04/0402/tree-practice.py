#SWEA5174
# def sol(start):
#     global cnt
#     if start:
#         cnt += 1
#         sol(c1[start])
#         sol(c2[start])
#
#
# tc = int(input())
#
# for _ in range(1, tc+1):
#     E, N = map(int, input().split())
#     arr = list(map(int, input().split()))
#     parent = [i for i in range(max(arr)+1)]
#     visited = [0] * len(parent)
#     c1 = [0] * len(parent)
#     c2 = [0] * len(parent)
#     for i in range(0, len(arr), 2):
#         if not c1[arr[i]]: c1[arr[i]] = arr[i+1]
#         else: c2[arr[i]] = arr[i+1]
#
#     cnt = 0
#     sol(N)
#
#     print(f'#{_} {cnt}')
''''''

# #SWEA5176
# AGAIN 아직 못 풀었음
# def sol(v):
#     if v <= n:
#         sol(2*v)
#         tree.append(v)
#         sol(2*v+1)
#
# def sol2(v):
#     if v <= n:
#         tree2.append(tree[v])
#         sol(2*v)
#         sol(2*v+1)
#
# tc = int(input())
# for _ in range(1, tc+1):
#     n = int(input())
#     nodes = [i for i in range(n+1)]
#     tree = []
#     sol(1)
#     tree.insert(0,0)
#     print(tree)
#     tree2 = [0] * (n+1)
#
#     for i in range(1, len(tree)):
#         tree2[i] = tree[i]
#     print(tree2)
#     # tree2 = []
#     # sol2(1)
#     # print(tree2)
#     # print(f'#{_} {tree[1]} {tree2[n//2]}')
'''
3
6
8
15
'''

#SWEA5177
# sol함수의 내부에서 최소힙을 유지하기 위해 parent node와 child node의 위치를 바꾸고 다음 child와 parent의 tree 내 idx를 정하는 과정을 잘못 적어서 fail이 계속 떴음.
# p = c//2 하고 c = p를 했는데, 이러면 제대로 다음 위치로 이동하지 못함.
# 우선 c=p를 하고 그 다음에 p=c//2를 해야됨
# def sol(num):
#     global last
#     last += 1
#     tree[last] = num
#     p = last//2
#     c = last
#     while p > 0 and tree[p] > tree[c]:
#         tree[p], tree[c] = tree[c], tree[p]
#         c = p
#         p = c//2
#
#
# tc = int(input())
# for _ in range(1, tc+1):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     tree = [0] * (n+1)
#     last = 0
#     for i in range(n):
#         sol(arr[i])
#
#     target = n
#     ans = 0
#     while target > 0:
#         target //= 2
#         ans += tree[target]
#
#     print(f'#{_} {ans}')


#SWEA5178
# tc = int(input())
#
# for _ in range(1, tc+1):
#     n, m, l = map(int, input().split())
#     tree = [0] * (n+1)
#     for i in range(m):
#         node, value = map(int, input().split())
#         tree[node] = value
#
#     c = n
#     while True:
#         if c == 1:
#             break
#         if c % 2:
#             tree[c//2] = tree[c] + tree[c-1]
#             c -= 2
#         else:
#             tree[c//2] = tree[c]
#             c -= 1
#
#     print(f'#{_} {tree[l]}')