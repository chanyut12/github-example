a=int(input())
b=float(input())
if a<60:
    if b<1000: #1.25%
        print("{:.2f}".format((b*1.25*(a/365))/100))  
    else: #1.6%
        print("{:.2f}".format((b*1.6*(a/365))/100))
elif 60<=a<=180:
    if b<5000: #1.5%
        print("{:.2f}".format((b*1.5*(a/365))/100))
    else: #1.95%
        print("{:.2f}".format((b*1.95*(a/365))/100))   
elif a>180: #1.8%
    if b<8000:
        print("{:.2f}".format((b*1.6*(a/365))/100))   
    else: #2.35%
        print("{:.2f}".format((b*2.35*(a/365))/100))         
else:
    print("error")