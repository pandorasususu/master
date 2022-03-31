#BOJ14888<연산자 끼워넣기>
#SWEA역량테스트

#일단 n! 시간복잡도를 조금 줄여서 통과함
# import itertools
#
# n = int(input())
# nums = list(map(int, input().split()))
#
# #연산자를 연속으로 cal_whole에 저장
# cal = list(map(int, input().split()))
# cal_whole = []
# for c in range(4):
#     if cal[c] == 0:
#         continue
#     repeat = cal[c]
#     while True:
#         cal_whole.append(c)
#         repeat -= 1
#         if repeat == 0:
#             break
# for c in range(len(cal_whole)):
#     if cal_whole[c] == 0:
#         cal_whole[c] = '+'
#     elif cal_whole[c] == 1:
#         cal_whole[c] = '-'
#     elif cal_whole[c] == 2:
#         cal_whole[c] = '*'
#     else:
#         cal_whole[c] = '/'
#
# cal_cnd = list(itertools.permutations(cal_whole, len(cal_whole)))
# cal_cnd = list(set(cal_cnd))
#
#
# ans_list = []
# for i in range(len(nums)):
#     ans_list.append(nums[i])
#     if i == len(nums)-1:
#         break
#     else:
#         ans_list.append(0)
#
#
# stack = []
# ans_cnd = []
# for cals in cal_cnd:
#     stack.append(ans_list[0])
#     for e in range(1, len(ans_list)):
#         if ans_list[e] == 0 or type(ans_list[e]) != int:
#             ans_list[e] = cals[e//2]
#         else:
#             num = stack.pop()
#             if ans_list[e-1] == '+':
#                 stack.append(num+ans_list[e])
#             elif ans_list[e-1] == '-':
#                 stack.append(num-ans_list[e])
#             elif ans_list[e-1] == '*':
#                 stack.append(num*ans_list[e])
#             elif ans_list[e-1] == '/':
#                 if num >= 0:
#                     stack.append(num//ans_list[e])
#                 else:
#                     num = abs(num)
#                     stack.append(-(num//ans_list[e]))
#
#         if e == len(ans_list) - 1:
#             ans = stack.pop()
#             ans_cnd.append(ans)
#
# # print(len(cal_cnd))
# # print(len(list(set(cal_cnd))))
# # print(len(ans_cnd))
#
# print(max(ans_cnd))
# print(min(ans_cnd))

#모범답안 참고해서 다시 풀어보기

n = int(input())
arr = list(map(int, input().split()))
cal = list(map(int, input().split()))
maxV = -(10**9)
minV = 10 ** 9

def dfs(prevV, idx, plus, minus, multi, divide):
    global minV, maxV
    if idx == n:
        if minV > prevV:
            minV = prevV
        if maxV < prevV:
            maxV = prevV

    else:
        if plus:
            dfs(prevV + arr[idx], idx + 1, plus - 1, minus, multi, divide)
        if minus:
            dfs(prevV - arr[idx], idx + 1, plus, minus - 1, multi, divide)
        if multi:
            dfs(prevV * arr[idx], idx + 1, plus, minus, multi - 1, divide)
        if divide:
            if prevV < 0:
                dfs(-(abs(prevV) // arr[idx]), idx + 1, plus, minus, multi, divide - 1)
            else:
                dfs(prevV // arr[idx], idx + 1, plus, minus, multi, divide - 1)


dfs(arr[0], 1, *cal)
print(maxV)
print(minV)
