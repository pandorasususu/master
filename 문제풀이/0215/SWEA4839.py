#SWEA4839<이진탐색>
#변수 이름을 중복되지 않게 설정하자.
T = int(input())

for _ in range(1, T+1):
    P, A, B = map(int, input().split())

    start_a = 1
    cnt_a = 1
    end_a = P
    while True:
        m_a = int((start_a + end_a)/2)
        if A > m_a:
            start_a = m_a
            cnt_a += 1
        elif A < m_a:
            end_a = m_a
            cnt_a += 1
        else:
            break

    start_b = 1
    cnt_b = 1
    end_b = P
    while True:
        m_b = (start_b + end_b) // 2
        if B > m_b:
            start_b = m_b
            cnt_b += 1
        elif B < m_b:
            end_b = m_b
            cnt_b += 1
        else:
            break

    if cnt_a < cnt_b:
        print(f'#{_} A')
    elif cnt_a > cnt_b:
        print(f'#{_} B')
    else:
        print(f'#{_} 0')

'''
1
1000 299 578

1000
500
250
375
312
281
296
304
300
298
299
'''