def change(n):
    a = []
    b = []
    for i in range(n):
        n = int(input())
        a.append(n) 
    for j in a:
        if j >=10:
            j+=1
            b.append(j)    
        else:
            j-=1
            b.append(j)  
    print("Before data")
    print(" ".join(map(str,a)))  
    print("After data")   
    print(" ".join(map(str,b)))    

n = int(input())
change(n)
