#BOJ14889<스타트와 링크>
#SWEA역량테스트

#두번째 시도
from itertools import combinations as cb
tc = int(input())
arr = [list(map(int, input().split())) for _ in range(tc)]
member = [i for i in range(tc)]

total = 0
#행렬 전체합 구하는 방법 1
# for row in range(tc):
#     for col in range(tc):
#         total += arr[row][col]

#행렬 전체합 구하는 방법 2 -> 1과 수행 시간 차이 없음
for i, j in zip(arr, zip(*arr)):
    total += sum(i) + sum(j)
total //= 2

first_team = list(cb(member,(tc//2)))
reverse_arr = list(zip(*arr))

diff = []
for ft in first_team:
    first_team_score = 0
    for ppl in ft:
        first_team_score += sum(arr[ppl]) + sum(reverse_arr[ppl])
    diff.append(abs(total - first_team_score))
print(min(diff))

# 첫 번째 시도
# #itertools.combinations 사용해서 부분집합 만들기
# first_team = list(cb(member,(tc//2)))
#
#
# #단순 반복문 이용해서 부분집합 만들기
# # subsets = [[]]
# # for num in member:
# #   size = len(subsets)
# #   for y in range(size):
# #     subsets.append(subsets[y]+[num])
# #
# # first_team = []
# # for sub in subsets:
# #     if len(sub) == (tc//2):
# #         first_team.append(sub)
#
# diff = []
# for ppl in range(len(first_team)):
#     first_team_score = 0
#     for row in first_team[ppl]:
#         for col in first_team[ppl]:
#             if row != col:
#                 first_team_score += arr[row][col]
#
#     second_team = []
#     for m in member:
#         if m not in first_team[ppl]:
#             second_team.append(m)
#
#     second_team_score = 0
#     for row in second_team:
#         for col in second_team:
#             if row != col:
#                 second_team_score += arr[row][col]
#
#     diff.append(abs(first_team_score - second_team_score))
#
# print(min(diff))


#모범답안
#각 팀의 능력치 차는 전체 능력치 행렬의 합에서, 한 팀의 능력치 행렬의 합을 차감한 것의 절대값과 같다.
#https://www.acmicpc.net/board/view/72643
'''
import sys
from itertools import combinations as cb
N = int(sys.stdin.readline()) // 2
M = 2*N
stat = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
newstat = [sum(i) + sum(j) for i, j in zip(stat, zip(*stat))]
allstat = sum(newstat) // 2

mins = 65535
for l in cb(newstat[:-1], N):
    mins = min(mins, abs(allstat - sum(l)))
print(mins)
'''
