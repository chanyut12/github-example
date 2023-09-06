n = int(input())
b=[]

for i in range(n):
    a = int(input())
    b.append(a)

c = sum(b)/len(b)
d=0
e=0
for i in b:
    if i>c:
        e+=1
    elif i<c:
        d+=1

print("Average :",c)
print("Lower :",d)
print("Higher :",e)