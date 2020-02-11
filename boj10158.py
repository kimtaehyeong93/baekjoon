# import sys
# sys.stdin = open("example.txt", "r")

# def issafe(q,p):
#     if q + dx[j] <= w or q + dx[j] >= 0 or p + dy[j] >= 0 or p + dy[j] <= h:
#         return True
#     return False

# def reverse(q,p):
#     if (q + dx[j] == w and p + dy[j] == 0) or (q + dx[j] == w and p + dy[j] == h) or (q + dx[j] == 0 and p + dy[j] == h) or (q + dx[j] == 0 and p + dy[j] == 0):
#         return True
#     return False
# w, h = map(int,input().split())
# p, q = map(int,input().split())
# t = int(input())
# p, q = h-q, p
# dx = [1, -1, -1, 1]
# dy = [-1, -1, 1, 1]
# j=0
# k=0
# p_list = [p]
# q_list = [q]
# j_list= [0]
# while True:
#     if 0 <= q <= w and 0 <= p <= h:
#         if issafe(q,p):
#             if reverse(q,p):
#                 k += 2
#             elif q + dx[j] == w and j == 0:
#                 k += 1
#             elif q + dx[j] == w and j ==3:
#                 k += 3
#             elif p + dy[j] == 0 and j == 1:
#                 k += 1
#             elif p + dy[j] == 0 and j == 0:
#                 k += 3
#             elif p + dy[j] == h and j == 2:
#                 k += 3
#             elif p +dy[j] == h and j == 3:
#                 k += 1
#             elif q + dx[j] == 0 and j == 1:
#                 k += 3
#             elif q + dx[j] == 0 and j == 2:
#                 k += 1

#     p = p + dy[j]
#     q = q + dx[j]
#     j = k % 4
#     if p_list[0] == p and q_list[0] == q and j_list[0] == j:
#         break
#     else:
#         p_list.append(p)
#         q_list.append(q)
#         j_list.append(j)

# if t <= len(p_list):
#     p = p_list[t]
#     q = q_list[t]
# else:
#     p = p_list[t % len(p_list)]
#     q = q_list[t % len(p_list)]
# print(q, h-p)

import sys
sys.stdin = open("example.txt", "r")

w, h = map(int,input().split())
p ,q = map(int,input().split())
t = int(input())
p_prime = t % (2*w)
q_prime = t % (2*h)
if q_prime <= h-q:
    q = q + q_prime
elif h-q < q_prime <= 2*h - q:
    q = (2*h) -q - q_prime
elif q_prime > 2*h -q:
    q = (q_prime-h) - (h-q)

if p_prime <= w-p:
    p = p + p_prime
elif w-p < p_prime <= 2*w - p:
    p =(2*w) -p -p_prime
elif p_prime > 2*w -p:
    p = (p_prime-w) - (w-p)

print(p, q)


