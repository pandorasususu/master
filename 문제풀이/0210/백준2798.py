#백준2798
'''
N, M = map(int, input().split())
card = list(map(int, input().split()))
m_diff = M
cnt = 0
for idx_1 in range(len(card)):
    for idx_2 in range(idx_1+1, len(card)):
        for idx_3 in range(idx_2+1, len(card)):
            card_sum = card[idx_1] + card[idx_2] + card[idx_3]
            if card_sum > M:
                continue
            else:
                card_sum_diff = M - card_sum
                if m_diff > abs(card_sum_diff):
                    m_diff = abs(card_sum_diff)
                    ans = card_sum

print(ans)
'''