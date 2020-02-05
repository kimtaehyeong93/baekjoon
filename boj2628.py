import sys
sys.stdin = open("example.txt","r")

x, y = map(int,input().split())
time = int(input())

num=[[i for i in map(int,input().split())] for j in range(time)]

w = [0, x]
h = [0, y]

for i in range(time):
    if num[i][0]:
        w.append(num[i][1])
    else:
        h.append(num[i][1])
w.sort()
h.sort()

ans=[]
for i in range(len(w)-1):
    for j in range(len(h)-1):
        ans += [(w[i+1]-w[i])*(h[j+1]-h[j])]

print(max(ans))

