
def permu(a):
    for i in range(len(a)):
        if visited[i] == 0:
            temp.append(a[i])
            visited[i] = 1
            permu(a)
            visited[i] = 0
            temp.pop()
    if len(temp) == 4:
        lst.append(temp[:])


b = [1, 2, 3,4]
lst = []
temp = []
visited = [0] * 4

permu(b)
print(lst)






    

