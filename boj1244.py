import sys
sys.stdin = open("example.txt","r")

N = int(input())
status = list(map(int,input().split()))
num = int(input())
student = []
for i in range(num):
    student.append(list(map(int,input().split())))

for i in range(num):
    m = 0
    if student[i][0] == 1:
        x = student[i][1]
        for j in range(N):
            if (j+1) % x == 0:
                if status[j] == 0:
                    status[j] = 1
                else:
                    status[j] = 0
    else:
        y = student[i][1]
        while True:
            if y-1+m > N-1 or y-1-m < 0:
                break
            if status[y-1+m] != status[y-1-m]:
                break
            m += 1
        if status[y-1] == 0:
            status[y-1] = 1
        else:
            status[y-1] = 0
        if m != 0:
            for j in range(1,m):

                if status[y-1+j] == 0:
                    status[y-1+j] = 1
                else:
                    status[y-1+j] = 0

                if status[y-1-j] == 0:
                    status[y-1-j] = 1
                else:
                    status[y-1-j] = 0

iter = int(N/20)
for j in range(iter+1):
    print(' '.join([str(r) for r in status[20*j:20*j+20]]))





