#BOJ14501<퇴사>
#SWEA역량테스트

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
reward = [0] * (N+1)
ans_list = []
for idx in range(N-1, -1, -1):
    if arr[idx][0] + idx > N:
        reward[idx] = reward[idx+1]
    else:
        reward[idx] = max(reward[idx+1], arr[idx][1] + reward[idx+arr[idx][0]])

print(reward[0])


''' 동적계획법
https://cocook.tistory.com/m/11
'''
n = int(input())
t = [0] * (n + 1) #i번쨰 날 수행하는 상담 기간
p = [0] * (n + 1) #i번째 상담을 수행 했을 때 받는 페이
dp = [0] * (n + 2) # 메모이제이션 : i번째 날 상담을 수행 했을 때 받을 수 있는 최대 페이

for i in range(1, n + 1):
    t[i], p[i] = map(int, input().split()) #입력

for i in range(n, 0, -1): #뒤쪽에서부터 업데이트
    next = i + t[i] # i번째 상담을 수행했을 때 다음 상담을 수행 할 수 있는 날짜
    #
    # dp[i] = dp[i + 1] if next > n + 1 else max(dp[i + 1], dp[next] + p[i])

    if next > n + 1:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[next]+p[i])
	# 다음 수행 날짜가 n+1보다 크면 전 날(i+1) 값으로 업데이트
    # 아니라면 전날 값과 i번째 날 상담을 수행했을 때 값을 비교해 업데이트

print(dp[1])


'''DFS
N=int(input())
S=[0 for i in range(N)]
P=[0 for i in range(N)]
for i in range(0,N):
    S[i], P[i] = map(int, input().split())

ans =0

def solve(day, profit):
    if day == N: #퇴사 날이 되면 수익을 업데이트 해준다.
        global ans
        ans = max(profit, ans)
        return

    if day + S[day] <= N: #day의 상담을 먹는 경우
        solve(day + S[day], profit+P[day]) #

    solve(day + 1, profit) #안먹는 경우

solve(0, 0)
print(ans)
'''
