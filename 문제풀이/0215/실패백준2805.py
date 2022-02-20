#백준2805<나무 자르기>
#구현은 한 것 같은데 시간복잡도에서 걸리는 것 같다.

N, M = map(int, input().split())
tree_list = list(map(int, input().split()))
tree_list.sort(reverse=True)
ax = tree_list[0]

for i in range(ax):


sum_t = 0

while True:
    for t in tree_list:
        if t - ax > 0:
            sum_t += t - ax
        else:
            break
    if sum_t >= M:
        break
    else:
        ax -= 1
        sum_t = 0
print(ax)
