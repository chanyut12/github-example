n = int(input())
m = int(input())
def fac(n):
    if n==0:
        return 1
    return n * fac(n-1)


fac(n)
def G(n,m):
    if m>n:
        return -1
    elif m==n:
        return 1
    return m*G(n,m+1)

print(G(n,m))