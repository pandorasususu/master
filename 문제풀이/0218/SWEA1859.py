#SWEA1859<백만장자프로젝트>

T = int(input())
for _ in range(1,T+1):
    N = int(input())
    days = list(map(int, input().split()))

    cnt = 0
    ans = 0
    max_area_num = len(days)-1
    for d in range(len(days)-2, -1,-1): #가장 마지막 날 부터 출발
        if days[max_area_num] < days[d+1]: #가격이 마지막 날의 가격보다 높을지 판단 
            max_area_num = d+1
        if days[d] <= days[d+1] or days[d] < days[max_area_num]: #오늘의 가격이 내일보다 낮거나 최대가격보다 낮을 경우 최대가격에서 오늘의 가격의 차를 최종 답에 더함
            ans += days[max_area_num] - days[d]

    print(f"#{_} {ans}")

''' 이전에 풀었던 코드
a = int(input())
for b in range(a):
    c = int(input())
    my_list = list(map(int, input().split()))[::-1]
    sum_money = 0
    now_max = my_list[0]
    for e in range(1, c):
        if now_max > my_list[e]:
            sum_money += (now_max - my_list[e])
        else:
            now_max = my_list[e]
    print(f'#{b+1} {sum_money}')
249,164 kb
메모리
1,116 ms
실행시간
338
코드길이
'''


