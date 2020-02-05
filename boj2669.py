import sys
sys.stdin = open("example.txt", "r")

N = []
cnt = 0
for i in range(4):
    N.append(list(map(int,input().split())))

background = [[0 for i in range(100)] for j in range(100)]

for i in range(4):
    lenx = list(range(N[i][0],N[i][2]))
    leny = list(range(N[i][1],N[i][3]))
    for j in lenx:
        for k in leny:
            background[j][k] = 1
for i in range(100):
    cnt += background[i].count(1)

print(cnt)



