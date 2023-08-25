a = int(input())
b=1
d=a-1
c = a
for i in range(a):
    for j in range(d):
        print("", end=" ")
    for k in range(b):
        print("", end="*")
    print()    
    b+=1
    d-=1


