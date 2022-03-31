#BOJ13458<시험 감독>
#SWEA 역량테스트
#반복문 돌리는 것을 최소하하자
N = int(input())
arr = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = 0

for ppl in arr:
    if ppl <= B:
        cnt += 1
        continue
    else:
        ppl -= B
        cnt += 1
        sub = divmod(ppl, C)
        if sub[1] != 0:
            cnt += sub[0] + 1
        else:
            cnt += sub[0]

print(cnt)



