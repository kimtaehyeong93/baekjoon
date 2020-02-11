import sys
sys.stdin = open("example.txt")

def rotate_right(x):
    length = len(x)
    temp = [[] for i in range(length)]
    for i in range(length):
        for j in range(length-1,-1,-1):
            temp[i] += [x[j][i]]
    return temp


T = int(input())
for t in range(T):
    N = int(input())
    n = int((N - 1)/2)
    mymap = []
    for _ in range(N):
        mymap += [list(map(int,input()))]
    sum_total = 0
    for i in range(N):
        for j in range(N):
            sum_total += mymap[i][j]
    sum_minus = 0

    for i in range(n):
        for j in range(i,n):
            sum_minus += mymap[i][j-i]

    for _ in range(3):
        mymap = rotate_right(mymap)
        for i in range(n):
            for j in range(i,n):
                sum_minus += mymap[i][j-i]
    
    print('#{0} {1}'.format(t+1, sum_total - sum_minus))