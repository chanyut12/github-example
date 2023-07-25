a=input()
b=float(input())
if a=="h":
    if b<200: #1.75
        print("{:.2f}".format(b*1.75))
    else: #2.00
        print("{:.2f}".format(b*2.00))
elif a=="d":
    if b<200: #2.5
        print("{:.2f}".format(b*2.5))
    else: #2.75
        print("{:.2f}".format(b*2.75))      
else:
    print("Error")        
