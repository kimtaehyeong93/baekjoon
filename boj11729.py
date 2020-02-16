n = int(input())
def hanoi(n, ffrom, to, empty):
    if n == 1:
        ans = [ffrom, to]
        print(*ans)
        return
    else:
        hanoi(n-1,ffrom,empty,to) 
        hanoi(1,ffrom,to,empty)
        hanoi(n-1,empty,to,ffrom) 
        return   
print(2**n - 1)
hanoi(n,1,3,2)