a=int(input())
b=int(input())
new_list=[]
for j in range(1,b+1):
    new_list.append(j)

for k in range(1, a+1):
    for i in new_list:
        print(i, end=" ")
    print()    



