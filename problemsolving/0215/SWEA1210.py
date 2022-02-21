#SWEA1210<ladder1>
#문제 잘 읽는 것의 중요성
#사다리타기를 해서 마지막 행에 2에 도달하는 모든 경우의 수를 구하라는 것으로 이해하고 풀었더니 너무 어려웠음.
#사실은 그냥 단순히 사다리타기 게임에서 당첨되는 첫행의 위치를 구하를 문제였음.

T = 10
for idx in range(1,T+1):
    N = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)] #이동하다가 범위를 벗어나는 것을 방지하기위해 좌우 가장자리에 0 삽입

    for e in range(102): #양 옆에 0으로만 이루어진 열이 삽입되어 있기 때문
        if arr[0][e] == 1:
            r, c = 0, e

            while r < 99: #r이 99보다 작을 경우

                if arr[r][c+1]: #오른쪽에 1이 있으면 0을 만날 때까지 오른쪽으로 이동
                    while True:
                        c += 1
                        if arr[r][c+1] == 0:
                            break

                elif arr[r][c-1]:  #왼쪽에 1이 있으면 0을 만날 때까지 왼쪽으로 이동
                    while True:
                        c -= 1
                        if arr[r][c-1] == 0:
                            break
                r += 1 #그 외에는 아래로 이동

            if arr[r][c] == 2:
                print(f'#{idx} {e-1}') #양 옆에 0이 삽입되었으므로 1을 빼준 위치 반환