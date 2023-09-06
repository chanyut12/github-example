n = int(input())
b=[]
d=0
for i in range(n):
    a = int(input())
    b.append(a)

c = int(input())
for j in b:
    if c==j:
        d+=1

print(d)