m = int(input())
n = int(input())
def A(m,n):
    if m>n :
        return -1
    elif m==n:
        return 1
    else:
        return m * A(m+1,n)

print(A(m,n))     