N = int(input())
length = []
ans=[]

for i in range(int(N/2),N+1):
    num = []
    num += [N]
    num += [i]
    j = 2
    while True:
        num += [num[j-2] - num[j-1]]
        if num[-1] < 0:
            del num[-1]
            length += [len(num)]
            ans.append(num)
            break
        else:
            j += 1
max_num = max(length)
idx = length.index(max_num)
print(max_num)
print(' '.join([str(r) for r in ans[idx]]))


