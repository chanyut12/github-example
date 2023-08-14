a=str(input())
if a[:2]=="SC":
    print("Science Building")
elif a[:2]=="PY":
    print("Physics Building")    
elif a[:2]=="EN":
    print("Engineering Buliding")    
print("Floor",a[2]) 
print("Room",a[3:5])  