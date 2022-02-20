#SWEA1204<최빈수 구하기>
'''
n= int(input())
for _ in range(n):
    a = int(input())
    big_numbers = list(map(int, input().split()))
    big_numbers_unique = set(big_numbers) #받아온 숫자들 중 중복되는 것들은 제외, 내장함수 사용
    ans_dict={}
    for num in big_numbers_unique: #입력된 숫자들 중 중복되지 않은 값을 key로, 해당 값이 중복된 횟수를 value로 갖는 딕셔너리 생성
        ans_dict[num] = big_numbers.count(num)
    v_list = ans_dict.values()
    ans_max = max(v_list) #최빈수가 등장한 횟수 구하기, 내장함수 사용
    fin_ans=[]
    for k,v in ans_dict.items(): #최빈수가 등장한 횟수와 동등한 횟수로 등장한 수들 구하기
        if ans_dict[k] == ans_max:
            fin_ans.append(k)
    if len(fin_ans) == 1: #최빈수가 하나인 경우
        print(f'#{a} {fin_ans[0]}')
    else: #최빈수가 여러개인 경우, 가장 큰 값
        print(f'#{a} {max(fin_ans)}')
'''