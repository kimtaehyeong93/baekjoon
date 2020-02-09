import sys
sys.stdin = open("example.txt", "r")

x, y = map(int,input().split())
num = int(input())
mymap = [[0]*x for j in range(y)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
x_st = 0
y_st = y - 1
k = 0
j = 0
for i in range(1,x*y+1):
    if 0 <= y_st <= y and 0 <= x_st <= x:
        mymap[y_st][x_st] = i
        if 0 > y_st + dy[j] or y_st + dy[j] > y-1 or x_st + dx[j] < 0 or x_st + dx[j] > x-1:
            k += 1
        elif mymap[y_st+dy[j]][x_st+dx[j]]:
            k += 1
        j = k % 4
        y_st = y_st + dy[j]
        x_st = x_st + dx[j]

for i in range(x):
    for j in range(y):
        if mymap[j][i] == num:
            x_temp = i
            y_temp = j
            break
if num > x*y:
    print(0)
else:
    print(x_temp+1, y-y_temp)






