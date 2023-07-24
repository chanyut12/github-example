import math
a=input()
b=float(input())
c=float(input())
sum1=b+c
negative=b-c
times=b*c
if a=="*":
    print("{:.2f}".format(times))
elif a=="-":
    print("{:.2f}".format(negative))    
elif a=="+":
    print("{:.2f}".format(sum1)) 
elif a=="/":
    print("{:.2f}".format(b/c))     
else:
    print("Incorrect Symbol")     