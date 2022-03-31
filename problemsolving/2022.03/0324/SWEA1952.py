#1952. [모의 SW 역량테스트] 수영장

#그리디 알고리즘 2022.03.27
tc = int(input())
for _ in range(1, tc+1):
    day, month, month3, year = map(int, input().split())
    plan = [0] + list(map(int, input().split()))
    greedy = [0] * 13

    for i in range(1,13):
        minV = greedy[i-1] + plan[i] * day
        minV = min(minV, greedy[i-1] + month)

        if i >= 3:
            minV = min(minV, greedy[i-3] + month3)

        if i >= 12:
            minV = min(minV, greedy[i-12] + year)
        greedy[i] = minV
    print(f'#{_} {greedy[12]}')

#DFS 2022.03.27
# tc = int(input())
#
# def sol(idx, total_price):
#     global minV
#     if idx > 12:
#         if minV > total_price:
#             minV = total_price
#
#     # sol(idx+1, total_price + plan[idx] * day)
#     # sol(idx+1, total_price + month)
#     # sol(idx+3, total_price + month3)
#     # sol(idx+12, total_price + year)
#
#     else:
#         total_price += plan[idx] * day
#         sol(idx + 1, total_price)
#         total_price -= plan[idx] * day
#
#
#         total_price += month
#         sol(idx + 1, total_price)
#         total_price -= month
#
#
#         total_price += month3
#         sol(idx + 3, total_price)
#         total_price -= month3
#
#         total_price += year
#         sol(idx + 12, total_price)
#
# for _ in range(1, tc+1):
#     day, month, month3, year = map(int, input().split())
#     plan = [0] + list(map(int, input().split()))
#     minV = year * 365
#     sol(1, 0)
#
#     print(f'#{_} {minV}')


