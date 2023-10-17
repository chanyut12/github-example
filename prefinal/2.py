n = int(input())
def A(n):
    a = []
    c = 0
    for i in  range(n):
        b = int(input())
        a.append(b)    
    print(max(a))
    
    for j in a:
        if j == max(a):
            c+=1
    print(c)        

A(n)
