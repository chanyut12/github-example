a=str(input())
b=0

if 3<=len(a)<=5:
    for i in range(len(a)):
        if a[i]=="1":
            b+=1
    print(b)        

elif len(a)<3:
    print("Too short")

else:
    print("Too long")
