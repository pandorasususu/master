#BOJ1052<물병>
# ibm = initial bottle num
# cp = capacity
# ibm, cp = map(int, input().split())
# cnt = 0
# trial = 1
# while ibm != cp:
#     leftover = ibm % 2
#     ibm //= 2
#     # print('1',ibm, leftover,  cnt)
#     if leftover:
#         cnt += trial
#         ibm += 1
#         trial *= 2
#
#     # print('2', ibm, leftover, cnt)
#
# print(cnt)
# 13 3
# 11


# 백만 1 / 50만 2/ 25만 4/ 12만5천 8/ 62,500 16 / 31,250 32/  15625 64 /
# 7812 128 나머지 128 / 3906 256 / 1953 512 / 976 1024 나머지 1024
#
# 백만 = 2 ** 6 * 5 ** 6
#
# 백만 //
# 2십만 => 2 * 32 * 3125
#  => 64 * (1024 * 2 + 1077)
#  =>
# 15808 = 64 * 13 * 19
# 1,015,808 = 2 ** 15 * 31

ibm, cp = map(int, input().split())
i = 0
while True:
    if (cp * 2**i <= ibm) and (cp * 2**(i+1) > ibm):
        print(min(cp * 2**(i+1) - ibm, cp * 2**i - ibm))
        break
    else:
        print(cp * 2**i, cp * 2**(i+1))
        i += 1

2 2
4 4
8 8
12