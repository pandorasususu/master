#SWEA4836<색칠하기>
#제목에서 힌트를 얻었다.
#처음에는 겹치는 좌표를 구하고 그 넓이를 구하는 접근 방법을 택했지만, 지나치게 복잡해졌다.
#칠해진 횟수를 표시하면 덧칠해진 부분을 구할 수 있을 것이라 생각했다.
T = int(input())

for idx in range(1, T+1):
    N = int(input())
    base = [[0] * 10 for _ in range(10)] #아무것도 칠하지 않은 공간 표시
    arr_r = []
    arr_b = []
    for _ in range(N):
        ex = list(map(int, input().split()))
        if ex[-1] == 1:
            arr_r.append(ex)
        else:
            arr_b.append(ex)

    for i in range(len(arr_r)): #red로 칠한 부분을 우선 1로 표시
        rx1, ry1, rx2, ry2 = arr_r[i][0],arr_r[i][1],arr_r[i][2],arr_r[i][3]
        for rr in range(rx1, rx2 + 1):
            for rc in range(ry1, ry2 + 1):
                base[rr][rc] += 1

    for j in range(len(arr_b)): #blue로 칠한 부분에 1을 더함. 만약 이미 red가 칠해진 공간이라면 해당 공간의 값은 2가 될 것
        bx1, by1, bx2, by2 = arr_b[j][0],arr_b[j][1],arr_b[j][2],arr_b[j][3]
        for br in range(bx1, bx2 + 1):
            for bc in range(by1, by2 + 1):
                base[br][bc] += 1

    cnt = 0
    for r in range(10): #색이 겹친 부분의 개수를 구함
        for c in range(10):
            if base[r][c] == 2:
                cnt += 1
    print(f'#{idx} {cnt}')




