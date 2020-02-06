import sys
sys.stdin = open("example.txt", "r")
num = int(input())
length = [[i for i in map(int,input().split())] for j in range(6)]

x = []
y = []
x_now = 0
y_now = 0

for i in range(6):
    if length[i][0] == 4:
        x += [x_now + 0]
        y += [y_now + length[i][1]]
        y_now = y[i]
    elif length[i][0] == 2:
        x += [x_now - length[i][1]]
        y += [y_now + 0]
        x_now = x[i]
    elif length[i][0] == 3:
        x += [x_now + 0]
        y += [y_now - length[i][1]]
        y_now = y[i]
    elif length[i][0] == 1:
        x += [x_now + length[i][1]]
        y += [y_now + 0]
        x_now = x[i]

x_len = abs(max(x) - min(x))
y_len = abs(max(y) - min(y))
x_max = max(x)
x_min = min(x)
y_max = max(y)
y_min = min(y)
coordi = []
for i in range(6):
    coordi.append([x[i],y[i]])
    if x_min < x[i] < x_max and y_min < y[i] < y_max:
        x_2 = x[i]
        y_2 = y[i]

if [x_max, y_max] not in coordi:
    x_1 = x_max
    y_1 = y_max
elif [x_max, y_min] not in coordi:
    x_1 = x_max
    y_1 = y_min
elif [x_min, y_max] not in coordi:
    x_1 = x_min
    y_1 = y_max
elif [x_min, y_min] not in coordi:
    x_1 = x_min
    y_1 = y_min

s = num * ((x_len * y_len) - (abs(x_1 - x_2)*abs(y_1 - y_2)))
print(s)