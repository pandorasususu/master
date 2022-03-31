# tc = '0000000111100000011000000111100110000110000111100111100111111001100111'
#
# for idx in range(0, len(tc), 7):
#     block = tc[idx:idx+7]
#     ans = 0
#     for idx2 in range(6, -1,-1):
#         if block[idx2] == '1':
#             ans += 2 ** (6-idx2)
#     print(block, ans)

# tc = '0F97A3'
tc = '01D06079861D79F99F'
change = {
    '0':0,
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    'A':10,
    'B':11,
    'C':12,
    'D':13,
    'E':14,
    'F':15
}
t = len(tc) - 1
ans = ''
for chr in tc:
    a = str(bin(change[chr]))[2:]

    while len(a) != 4:
        a = '0' + a
    ans += a
    t -= 1

for idx in range(0, len(ans), 7):
    block = ans[idx:idx+7]
    fin_ans = 0
    for idx2 in range(len(block)-1, -1, -1):
        if block[idx2]=='1':
            fin_ans += 2 ** (len(block)-1-idx2)
    print(fin_ans, end=' ')