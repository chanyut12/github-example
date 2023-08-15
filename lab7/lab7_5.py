a=(input())
if a[:2]=="SC":
    print("Science Building")
    if 1<=int(a[2])<=9:
        print("Floor",a[2]) 
        if 1<= int(a[3:5])<=99: 
            print("Room",a[3:5])            
elif a[:2]=="PY":
    print("Physics Building")
    if 1<=int(a[2])<=9:
        print("Floor",a[2]) 
        if 1<= int(a[3:5])<=99: 
            print("Room",a[3:5])   
elif a[:2]=="EN":
    print("Engineering Building")
    if 1<=int(a[2])<=9:
        print("Floor",a[2]) 
        if 1<= int(a[3:5])<=99: 
            print("Room",a[3:5])            
