# import sys
# sys.stdin = open("example.txt", "r")

# N = int(input())
# A = []
# B = []
# for i in range(N):
#     A.append(list(map(int,input().split())))
#     B.append(list(map(int,input().split())))
# for i in range(N):
#     if A[i][1:].count(4) > B[i][1:].count(4):
#         print('A')
#     elif A[i][1:].count(4) < B[i][1:].count(4):
#         print('B')
#     else:
#         if A[i][1:].count(3) > B[i][1:].count(3):
#             print('A')
#         elif A[i][1:].count(3) < B[i][1:].count(3):
#             print('B')
#         else:
#             if A[i][1:].count(2) > B[i][1:].count(2):
#                 print('A')
#             elif A[i][1:].count(2) < B[i][1:].count(2):
#                 print('B')
#             else:
#                 if A[i][1:].count(1) > B[i][1:].count(1):
#                     print('A')
#                 elif A[i][1:].count(1) < B[i][1:].count(1):
#                     print('B')
#                 else:
#                     print('D')

import sys
sys.stdin = open("example.txt", "r")

N = int(input())
A = []
B = []
for i in range(N):
    A.append(list(map(int,input().split())))
    B.append(list(map(int,input().split())))

for i in range(N):
    a_sort = sorted(A[i][1:])
    a_sort.reverse()
    b_sort = sorted(B[i][1:])
    b_sort.reverse()
    a_len = A[i][0]
    b_len = B[i][0]
    d = a_len - b_len
    if d < 0:
        for j in range((-d)):
            a_sort += [0]
        for j in range(b_len):
            if a_sort[j] > b_sort[j]:
                print('A')
                break
            elif a_sort[j] < b_sort[j]:
                print('B')
                break
            elif j == b_len -1:
                print('D')
                break
                
        

    elif d > 0:
        for j in range(d):
            b_sort += [0]
        for j in range(a_len):
            if a_sort[j] > b_sort[j]:
                print('A')
                break
            elif a_sort[j] < b_sort[j]:
                print('B')
                break
            elif j == a_len - 1:
                print('D')
                break
    
    else:
        for j in range(a_len):
            if a_sort[j] > b_sort[j]:
                print('A')
                break
            elif a_sort[j] < b_sort[j]:
                print('B')
                break
            elif j == a_len - 1:
                print('D')
                break

        
    
     