import sys
sys.stdin = open("example.txt", "r")

num = int(input())

lst = []
bg = [0 for j in range(1,1000)]
for i in range(num):
    lst += list(map(int,input().split()))
start = lst[0]
finish = lst[-2]
for i in range(num):
    if lst[2*i] < start:
        start = lst[2*i]
    if lst[2*i] > finish:
        finish = lst[2*i]

for i in range(0,len(lst),2):
    bg[lst[i]] = lst[i+1]
bg = bg[start:finish+1]

rightend = len(bg) - 1
leftend = 0
h = max(bg)
idx = bg.index(h)
s = h
left = idx - 1
right = idx + 1
while left >= leftend:
    h = max(bg[:left+1])
    idx = bg.index(h)
    s += (left - idx + 1) * h
    left = idx - 1
while right <= rightend:
    h = max(bg[right:])
    idx = bg.index(h)
    s += (idx - right +1) * h
    right = idx + 1

print(s)









