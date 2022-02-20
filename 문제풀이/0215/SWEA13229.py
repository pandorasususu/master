#SWEA13229<일요일>
#13428과 같이 D3 레벨인데 난이도 차이가 너무 크게 느껴진다.
days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
b_days = [i.upper() for i in days]

T = int(input())
for _ in range(1,T+1):
    day = input()
    ans = b_days.index(day)
    if ans == 6:
        print(f'#{_} 7')
    else:
        print(f'#{_} {6-ans}')

