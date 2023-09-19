def change1(n):
    a = []
    b = []
    for i in range(n):
        n = int(input())
        a.append(n) 
    A = int(input())    
    for j in a:
        if j%2==0:
            j+=A
            b.append(j)    
        else:
            j =0 
            b.append(j)  
    print(" ".join(map(str,b)))

n = int(input()) 
change1(n)             