a=int(input())
b=int(input())
c=int(input())
if a<b:
    if a<c:
        print("The lowest number is {}".format(a))
    else:
        print("The lowest number is {}".format(c)) 

elif b<c:
    if b<a:
        print("The lowest number is {}".format(b))
    else:
        print("The lowest number is {}".format(a)) 
elif c<a:
    if c<b:
        print("The lowest number is {}".format(c))        
