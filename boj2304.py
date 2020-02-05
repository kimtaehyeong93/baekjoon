import sys
sys.stdin = open("example.txt", "r")

num = int(input())

lst = []
bg = [0 for j in range(0,1001)]
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

h = max(bg)
idx = bg.index(h)
rightend = idx
leftend = idx
s = h
left = 1
right = len(bg)-2
leftmax = bg[0]
rightmax = bg[len(bg)-1]
while left <= leftend:
    h_left = bg[left]
    if h_left > leftmax:
        s += leftmax
        leftmax = h_left
        left += 1
    elif h_left <= leftmax:
        s += leftmax
        left += 1    
    
while right >= rightend:
    h_right = bg[right]
    if h_right > rightmax:
        s += rightmax
        rightmax = h_right
        right -= 1
    elif h_right <= rightmax:
        s += rightmax
        right -= 1

print(s)









