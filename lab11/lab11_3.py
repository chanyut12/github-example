n = int(input())
m = int(input())

def G(n,m):
    if m>n:
        return -1
    elif m==n:
        return 1
    return m*G(n,m+1)

print(G(n,m))
