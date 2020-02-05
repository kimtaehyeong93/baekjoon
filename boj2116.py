import sys
sys.stdin = open("example.txt","r")

num = int(input())

dice = [[i for i in map(int,input().split())] for j in range(num)]
def func(lst,number):
    idx = lst.index(number)
    if idx == 0:
        del_num = lst[5]
        lst.remove(number)
        lst.remove(del_num)
        return max(lst), del_num
    elif idx == 1:
        del_num = lst[3]
        lst.remove(number)
        lst.remove(del_num)
        return max(lst), del_num
    elif idx == 2:
        del_num = lst[4]
        lst.remove(number)
        lst.remove(del_num)
        return max(lst), del_num
    elif idx == 3:
        del_num = lst[1]
        lst.remove(number)
        lst.remove(del_num)
        return max(lst), del_num
    elif idx == 4:
        del_num = lst[2]
        lst.remove(number)
        lst.remove(del_num)
        return max(lst), del_num
    else:
        del_num = lst[0]
        lst.remove(number)
        lst.remove(del_num)
        return max(lst), del_num

ans = [[] for i in range(6)]
ans_sum = []

for i in range(1,7):
    lst = []
    now = i
    for k in range(num):
        lst.append([m for m in dice[k]])
    for j in range(num):
        temp, now = func(lst[j],now)
        ans[i-1].append(temp)
    ans_sum.append(sum(ans[i-1]))
print(max(ans_sum))



