import sys
sys.stdin = open("example.txt", "r")
num = int(input())
data = [[i for i in map(int,input().split())] for j in range(num)]
mymap = [[0]*101 for i in range(101)]
for i in range(num):
    for j in range(data[i][0], data[i][0] + data[i][2]):
        for k in range(data[i][1], data[i][1] + data[i][3]):
            mymap[k][j] += 1

ans = [0] * num
for i in range(num-1,-1,-1):
    for j in range(data[i][0], data[i][0] + data[i][2]):
        for k in range(data[i][1],data[i][1] +data[i][3]):
            if mymap[k][j] in range(1,i+2):
                ans[i] += 1
                mymap[k][j] = 0

for i in range(num):
    print(ans[i])