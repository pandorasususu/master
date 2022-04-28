# 13987. [모의 SW 역량테스트] 홈 방범 서비스 (제출용)
def solve_loop():  # 단순무식하지만, 꼼꼼하게 따져보면 제일 쉽게 접근하는 방법일수도 있습니다
    sol = 0
    for si in range(N):
        for sj in range(N):
            for k in range(1, 2 * N):
                cnt = 0
                for i in range(si - k + 1, si + k):
                    for j in range(sj - k + 1 + abs(i - si), sj + k - abs(i - si)):
                        if 0 <= i < N and 0 <= j < N and arr[i][j]:
                            cnt += 1
                if k * k + (k - 1) * (k - 1) <= cnt * M and sol < cnt:
                    sol = cnt
    return sol


def BFS(si, sj):  # 루프보다 효율적 => K를 늘려가면서 추가되는 부분만 카운트하기 때문에...
    q = []
    v = [[0] * N for _ in range(N)]
    sol = cnt = old = 0

    q.append((si, sj))
    v[si][sj] = 1
    if arr[si][sj]:
        cnt += 1

    while q:
        ci, cj = q.pop(0)
        if old != v[ci][cj]:
            old = v[ci][cj]
            if cost[v[ci][cj]] <= cnt * M and sol < cnt:
                sol = cnt

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
                if arr[ni][nj]:
                    cnt += 1
    return sol


def solve_bfs():
    sol = 0
    for si in range(N):
        for sj in range(N):
            t = BFS(si, sj)
            if sol < t:
                sol = t
    return sol


def solve_tbl():  # 테이블에 저장해놓고 활용하는 가장 좋은 풀이법입니다
    home = []
    sol = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                home.append((i, j)) #집의 위치를 home 리스트에 저장

    for si in range(N):
        for sj in range(N): #마을을 전부 순회하면서
            cnts = [0] * 40
            for ci, cj in home: #해당 좌표에서 집들까지의 거리를 cnts리스트에 저장
                dist = abs(si - ci) + abs(sj - cj) + 1 #왜 거리를 이렇게 표시하는지는, 서비스 영역이 늘어나는 모습을 보면 알 수 있음. 1을 더한 이유는, cnts와 cost가 1부터 시작하기 때문
                cnts[dist] += 1
            for i in range(1, 40): #최대한의 집을 포함하는 범위를 구하기 위한 작업
                cnts[i] += cnts[i - 1]

            for k in range(1, 40):
                if cost[k] <= cnts[k] * M and sol < cnts[k]:
                    sol = cnts[k]
    return sol


cost = [0] + [k * k + (k - 1) * (k - 1) for k in range(1, 40)]
T = int(input())
# T = 10
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # ans = solve_loop()
    # ans = solve_bfs()
    ans = solve_tbl()
    print(f'#{test_case} {ans}')
