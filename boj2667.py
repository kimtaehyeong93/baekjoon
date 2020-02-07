import sys
sys.stdin = open("example.txt", "r")

def DFS(y,x):
    m += 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    k = 0
    m = 2
    if 0 <= y+dy[k] <= num - 1 and 0 <= x+dx[k] <= num - 1:
        if mymap[y+dy[k]][x+dx[k]] == 1:
            mymap[y + dy[k]][x + dx[k]] = m
            y = y + dy[k]
            x = x + dx[k]
            DFS(y,x)
        else:
            k += 1
    else:
        k += 1


num = int(input())

mymap = [[i for i in input()] for j in range(num)]

for i in range(num):
    for j in range(num):
        mymap[i][j] = int(mymap[i][j])
