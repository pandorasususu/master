#BOJ21608<상어초등학교>
#SWEA역량테스트
#2022.03.15 로직은 맞았지만 누더기처럼 이어붙인 것이고, 결과적으로 시간초과 뜸
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n**2)]
seats = [[0] * n for _ in range(n)]

def second(*nxt):
    empty_seats = [[0]*n for _ in range(n)]
    for r, c in nxt:
        for dr, dc in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
            new_r = r + dr
            new_c = c + dc
            if 0 <= new_r < n and 0 <= new_c < n:
                if seats[new_r][new_c] == 0:
                    empty_seats[r][c] += 1

    empty_list = []
    for row in range(n):
        for col in range(n):
            empty_list.append(empty_seats[row][col])
    empty_list.sort(reverse=True)
    maxV = max(empty_list)

    nxt2 = []
    for a, b in nxt:
        nxt2.append([a, b])
    nxt2.sort()
    idx = 0
    fin_list = []
    for e in empty_list:
        for r, c in nxt:
            if empty_seats[r][c] == e and not seats[r][c]:
                return [r, c]


def first(std, fav):
    my_seats = [[0] * n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            for dr, dc in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
                new_r = row + dr
                new_c = col + dc
                if 0 <= new_r < n and 0 <= new_c < n and not seats[row][col]:
                    if seats[new_r][new_c] in fav:
                        my_seats[row][col] += 1

    fav_list = []
    for seat in my_seats:
        fav_list.extend(seat)

    if fav_list.count(max(fav_list)) == 1:
        rowcol = fav_list.index(max(fav_list))
        row, col = divmod(rowcol, n)
        seats[row][col] = std
    else:
        nxt = []
        for idx in range(len(fav_list)):
            if fav_list[idx] == max(fav_list):
                row, col = divmod(idx, n)
                nxt.append([row, col])
        place = second(*nxt)
        seats[place[0]][place[1]] = std

for s in range(len(arr)):
    std, fav = arr[s][0], arr[s][1:]
    first(std, fav)

ans = 0
for e in arr:
    for row in range(n):
        for col in range(n):
            if e[0] == seats[row][col]:
                near = 0
                for dr, dc in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
                    new_r = row + dr
                    new_c = col + dc
                    if 0 <= new_r < n and 0 <= new_c < n:
                        if seats[new_r][new_c] in e[1:]:
                            near += 1
                if near == 0:
                    ans += 0
                elif near == 1:
                    ans += 1
                elif near == 2:
                    ans += 10
                elif near == 3:
                    ans += 100
                elif near == 4:
                    ans += 1000
print(ans)