a=0
b=0
c=0
while a >= 0:
    a=int(input())
    if a>60:
        b+=1
    elif 0<a<=60:
        c+=1
print(b)
print(c)            