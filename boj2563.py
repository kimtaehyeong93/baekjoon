import sys
sys.stdin = open("example.txt", "r")
N = int(input())
data = [[i for i in map(int,input().split())] for j in range(N)]

mymap = [[0] * (100) for i in range(100)]
for i in range(N):
    for j in range(10):
        for k in range(10):
            mymap[data[i][0]+j][data[i][1]+k] = 1
ans = 0
for i in range(100):
    ans += mymap[i].count(1)

print(ans)