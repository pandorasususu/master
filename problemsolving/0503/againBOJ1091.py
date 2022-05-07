#BOJ1091<카드섞기>

'''
p: 2 0 1
-> final: 1 2 0

s: 1 2 0
s0: 0 1 2
s1: 2 0 1
s2: 1 2 0


p: 0 1 2 0 1 2
-> final: 03 14 25

s: 1 4 0 3 2 5
so: 03 14 25

예제4
0: 357 11
1: 016 10
2: 2489
'''

card_num = int(input())
cards = [i for i in range(card_num)]

player0 = set()
player1 = set()
player2 = set()
target_rule = list(map(int, input().split()))

for idx_t in range(len(target_rule)):
    if target_rule[idx_t] == 0:
        player0.add(cards[idx_t])
    elif target_rule[idx_t] == 1:
        player1.add(cards[idx_t])
    else:
        player2.add(cards[idx_t])

# target = []
#
# for _0 in player0:
#     target.append(_0)
# for _1 in player1:
#     target.append(_1)
# for _2 in player2:
#     target.append(_2)

shuffle_rule = list(map(int, input().split()))
shuffle_cnt = 0

cts = cards[:]
result = -1
history = []
while True:
    player_00 = set()
    player_11 = set()
    player_22 = set()
    for idx_z in range(len(cts)):
        if idx_z % 3 == 0:
            player_00.add(cts[idx_z])
        elif idx_z % 3 == 1:
            player_11.add(cts[idx_z])
        else:
            player_22.add(cts[idx_z])

    if player0 == player_00 and player1 == player_11 and player2 == player_22:
        result = shuffle_cnt
        break
    else:
        zeros = [0] * card_num
        for idx in range(len(shuffle_rule)):
            zeros[shuffle_rule[idx]] = cts[idx]
        if zeros in history:
            break
        cts = zeros[:]
        history.append(cts)
        shuffle_cnt += 1

print(result)