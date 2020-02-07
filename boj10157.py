import sys
sys.stdin = open("example.txt", "r")

x, y = map(int,input().split())
mymap = [[0]*x for j in range(y)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
x_st = 0
y_st = y
k = 0
j = k % 4
for i in range(1,x*y+1):
    if 0 <= y_st + dy[j] <= y and 0 <= x_st + dx[j] <= x and not mymap[y_st+dy[j]][x_st+dx[j]]:
        mymap[y_st][x_st] = i
        y_st = y_st + dy[j]
        x_st = x_st + dx[j]

    else:
        k += 1
        mymap[y_st + i * dy[j]][x_st + i * dx[j]] = i



