# import sys
# sys.stdin = open("example.txt", "r")
#
# for tc in range(4):
#     data = list(map(int,input().split()))
#     x = max(data[2],data[6])
#     y = max(data[3],data[7])
#     mymap = [[0]*(x+1) for i in range(y+1)]
#     for k in range(0,5,4):
#         for i in range(data[k],data[k+2]+1):
#             for j in range(data[k+1],data[k+3]+1):
#                 mymap[j][i] += 1
#
#     ans_low=[0]*(y+1)
#     ans_col=[0]*(x+1)
#
#     for i in range(y+1):
#         ans_low[i] = mymap[i].count(2)
#     for j in range(x+1):
#         for i in range(y+1):
#             if mymap[i][j] == 2:
#                 ans_col[j] += 1
#     mymap.clear()
#     cnt_low = 0
#     cnt_col = 0
#
#     for i in range(y+1):
#         if ans_low[i]:
#             cnt_low += 1
#     for j in range(x+1):
#         if ans_col[j]:
#             cnt_col += 1
#
#     if cnt_low == 0 and cnt_col == 0:
#         print('d')
#     elif cnt_low == 1 and cnt_col == 1:
#         print('c')
#     elif cnt_low == 1 and cnt_col > 1:
#         print('b')
#     elif cnt_low > 1 and cnt_col == 1:
#         print('b')
#     else:
#         print('a')
#
import sys
sys.stdin = open("example.txt", "r")

for tc in range(4):
    data = list(map(int,input().split()))

    x1, x2, x3, x4 = data[0], data[2], data[4], data[6]
    y1, y2, y3, y4 = data[1], data[3], data[5], data[7]

    if (x2, y2) == (x3, y3) or (x1, y1) == (x4, y4) or (x2, y1) == (x3, y4) or (x1, y2) == (x4, y3):
        print('c')
    elif x3 > x2 or y3 > y2 or x1 > x4 or y1 > y4:
        print('d')
    elif y1 == y4 or y2 == y3 or x2 == x3 or x1 == x4:
        print('b')
    else:
        print('a')