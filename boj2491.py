import sys
sys.stdin = open("example.txt", "r")

N = int(input())
seq = list(map(int,input().split()))
j = 0
maxnum = 1

while j < N-1:
    incre = 1
    decre = 1
    for i in range(j,N-1):
        if seq[i] <= seq[i+1]:
            incre += 1
            j += 1
        else:
            while True:
                if seq[j] == seq[j-1]:
                    j -= 1
                else:
                    break
            break
    for i in range(j,N-1):
        if seq[i] >= seq[i+1]:
            decre += 1
            j += 1
        else:
            while True:
                if seq[j] == seq[j-1]:
                    j -= 1
                else:
                    break
            break
    if incre > maxnum:
        maxnum = incre
    if decre > maxnum:
        maxnum = decre
print(maxnum)



        

