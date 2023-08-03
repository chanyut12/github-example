a=0
b=0
c=0
while 0<=a<=100:
    print("a ={}".format(a))
    a=int(input())
    print("a ={}".format(a))
    if a%2==0 and 0<=a<=100:
        b+=1
    elif a%2!=0 and 0<=a<=100:
        c+=1
print(b)
print(c)        
