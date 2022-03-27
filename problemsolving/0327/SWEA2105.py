#2105. [모의 SW 역량테스트] 디저트 카페



#실패
# tc = int(input())
#
# path = [[1,-1],[1,1],[-1,1],[-1,-1]]
#
# for _ in range(1,tc+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     maxV = 0
#     for r in range(N):
#         for c in range(N):
#             sr, sc = r, c
#             dessert = [arr[sr][sc]]
#             stack = [[sr, sc]]
#             idx = 0
#
#             while stack:
#                 test_r, test_c = stack[-1]
#                 next_r, next_c = test_r + path[idx][0], test_c + path[idx][1]
#
#                 if 0 <= next_r < N and 0 <= next_c < N and arr[next_r][next_c] not in dessert:
#                     stack.append([next_r, next_c])
#                     dessert.append(arr[next_r][next_c])
#
#                 else:
#                     if idx == 3:
#                         if next_r == sr and next_c == sc:
#                             break
#                         else:
#                             dessert = []
#                             break
#
#                     idx += 1
#                     turn_r, turn_c = next_r + path[idx][0], next_c + path[idx][1]
#                     if 0 <= turn_r < N and 0 <= turn_c < N and arr[turn_r][turn_c] not in dessert:
#                         stack.append([turn_r, turn_c])
#                         dessert.append(arr[turn_r][turn_c])
#                     else:
#                         stack.pop()
#                         dessert.pop()
#
#             if len(dessert) > maxV:
#                 maxV = len(dessert)
#
#     if maxV == 0:
#         maxV = -1
#
#     print(f'#{_} {maxV}')

'''
1              
4                
9 8 9 8
4 6 9 4
8 7 7 8
4 5 3 5
'''