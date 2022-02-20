#백준1181
import sys
input = sys.stdin.readline

T = int(input())
word = [input() for _ in range(T)]
word = list(set(word))
word.sort(key=len)

start_dict = {}
end_dict = {}
for e in range(len(word)):
    if len(word[e]) in end_dict.keys():
        end_dict[len(word[e])] += 1
    else:
        end_dict[len(word[e])] = e
        start_dict[len(word[e])] = e

k_list = list(start_dict.keys())

for w1 in range(len(word)):
    for k in k_list:
        if (len(word[w1]) == k) and (end_dict[k] - start_dict[k] != 0):
            for w2 in range(start_dict[k], end_dict[k]+1):
                for w3 in range(end_dict[k], w2, -1):
                    if word[w2] > word[w3]:
                        word[w2], word[w3] = word[w3], word[w2]

for idx in word:
    print(idx)


# print(word)
#
# print('it' > 'no')
# print('it' > 'im')
# print('no' > 'im')
#
# w_list = ['it', 'im','no']
# for jj in range(len(w_list)):
#     for jjj in range(len(w_list)-1, jj, -1):
#         if w_list[jj] > w_list[jjj]:
#             w_list[jj], w_list[jjj] = w_list[jjj], w_list[jj]
# print(w_list)

'''
it
wont
but
im
more
cannot
yours
no
wait
hesitate
i

4
aaa
aab
baa
aba
'''