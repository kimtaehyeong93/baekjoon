import sys
sys.stdin = open("example.txt", "r")

num, length = map(int,input().split())
lst = [ i for i in map(int,input().split())]

iter = num - length + 1
max_num = -10e10
ans = 0
i = 0
cnt = 0
time = 0
while True:
    ans += lst[i]
    cnt += 1
    if cnt == length:
        if ans > max_num:
            max_num = ans
        time += 1
        cnt = 0
        ans = 0
        i = time
        continue
    i += 1
    if time == iter:
        break
print(max_num)





