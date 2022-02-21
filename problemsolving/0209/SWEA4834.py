#SWEA4834<숫자카드>
'''
T = int(input())
for _ in range(1,T+1):
    N = int(input())
    card_list = list(map(int, input().strip()))
    max_card = card_list[0]
    for card in card_list:
        if max_card < card:
            max_card = card
    card_count = [0] * (max_card+1)
    for card in card_list:
        card_count[card] +=1

    max_count=card_count[0]
    for count in card_count:
        if max_count < count:
            max_count = count

    max_idx = 0
    for idx in range(len(card_count)):
        if card_count[idx] == max_count:
            if max_idx < idx:
                max_idx = idx
    print(f'#{_} {max_idx} {max_count}')
'''