#SWEA1220<Magnetic>
tc = 10

for _ in range(1, tc+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr = list(zip(*arr))

    #zip 함수 없이 행열 교환
    # for i in range(N):
    #     for j in range(N):
    #         if i < j:
    #             arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    cnt = 0
    row = col = 0
    
    #1이 존재하면 그 뒤로 1이 있을 경우는 고려하지 않고 2와 조우할 때만 교착상태 1증가
    #그리고 2의 위치로 옮겨서 그 뒤로 반복
    while 0<=row<N and 0<=col<N:
        nxt = False
        if arr[row][col] == 1:
            for c in range(col, N):
                if arr[row][c] == 1:
                    continue
                elif arr[row][c] == 2:
                    cnt += 1
                    col = c
                    nxt = True
                    break
        if nxt == True:
            continue
        col += 1

        if 1 not in arr[row][col:]:
            row += 1
            col = 0

    print(f'#{_} {cnt}')

