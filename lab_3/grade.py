a=int(input())
if a<0 or a>100:
    print("Please fill score again")
elif a<50:
    print("F")    
elif a<60:
    print("D")
elif a<70:
    print("C")
elif a<80:
    print("B")
else:
    print("A")                