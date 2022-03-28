#4366. 정식이의 은행업무

tc = int(input())

for _ in range(1, tc+1):
    two_list = list(map(int, input().strip()))
    three_list = list(map(int, input().strip()))
    fin_ans = 0
    for i in range(len(two_list)):
        two_list[i] = (two_list[i] + 1) % 2
        m2 = 0
        ans2 = 0
        for j in range(len(two_list)-1, -1, -1):
            ans2 += two_list[j] * (2 ** m2)
            m2 += 1
        #2진수를 10진수로 바꾸었을 때, 주어진 3진수에서 하나의 자리수만을 바꾸어 일치하는 3진수의 값을 탐색
        for k in range(len(three_list)):
            for l in range(1,3):
                three = three_list[:]
                three[k] = (three[k] + l) % 3

                m3 = 0
                ans3 = 0
                for m in range(len(three) - 1, -1, -1):
                    ans3 += three[m] * (3 ** m3)
                    m3 += 1

                if ans2 == ans3:
                    fin_ans = ans2
    
    #2진수를 10진수로 바꾸고, 다시 3진수로 바꾸어 주어진 3진수와 비교했을 때 자리수가 얼마나 다른지 비교, 답은 잘 나오는 거 같은데 제출하면 계속 runtime error 발생
    # ans3 = [0] * len(three_list)
    # change = ans2
    # position = 0
    # while change:
    #     ans3[position] = change % 3
    #     position += 1
    #     change //= 3
    # ans3 = ans3[::-1]
    # 
    # cnt = 0
    # for k in range(len(three_list)):
    #     if ans3[k] != three_list[k]:
    #         cnt += 1
    # 
    # if cnt == 1:
    #     fin_ans = ans2
    #     break
    # two_list[i] = (two_list[i] + 1) % 2

    print(f'#{_} {fin_ans}')
'''
5
1010
212
100110
1102
1011
102
110110111101
11212010
1000100000111100
1211012012

(36)
100100
1100

(9)
1001
100

(3513)
110110111001
11211010

(35132)
1000100100111100
1210012012
'''