import sys
sys.stdin = open("example.txt", "r")

lst = []
for i in range(9):
    lst.append(int(input()))
for i in range(9):
    for j in range(8):
        temp=[m for m in lst]
        del temp[i]
        del temp [j]
        if sum(temp) == 100:
            break
    if sum(temp) == 100:
        break
temp.sort()
for i in range(7):
    print(temp[i])
