# 5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용
#실행속도가 좀 느린 거 같아서 다시 풀어봄. visited 리스트만을 통해서 해결할 수 있었던 것을 과하게 복잡하게 접근했음.
# tc = int(input())
#
# def sol(idx, cost):
#     global min_cost
#     if idx >= N:
#         if cost < min_cost:
#             min_cost = cost
#     else:
#         for idx_f in range(N):
#             if factory[idx_f] not in perm:
#                 perm.append(factory[idx_f])
#                 cost += arr[idx][idx_f]
#                 if cost > min_cost:
#                     cost -= arr[idx][idx_f]
#                     perm.pop(idx)
#                     continue
#                 else:
#                     sol(idx+1, cost)
#                     cost -= arr[idx][idx_f]
#                     perm.pop(idx)
#
# for _ in range(1, tc+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     factory = [i for i in range(N)]
#     min_cost = 10 ** 10
#     perm = []
#     sol(0, 0)
#
#     print(f'#{_} {min_cost}')

#2022.04.02 다시 풀어보기
def sol(idx_product, cost):
    global minV
    if cost >= minV:
        return
    if cost < minV and idx_product >= p_num:
        minV = cost
        return

    for idx_factory in range(p_num):
        if not visited[idx_factory]:
            visited[idx_factory] = 1
            sol(idx_product+1, cost + arr[idx_product][idx_factory])
            visited[idx_factory] = 0

tc = int(input())
for _ in range(1, tc+1):
    p_num = int(input())
    visited = [0] * p_num
    arr = [list(map(int, input().split())) for _ in range(p_num)]
    minV = 100 * p_num
    sol(0, 0)

    print(f'#{_} {minV}')