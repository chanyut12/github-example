m = int(input())
n = int(input())

a_reverse = [['' for j in range(n)] for i in range(m)]

matrix = []

def create(m,n):
    for i in range(m):
        row = []
        for j in range(n):
            col = input()
            row.append(col)
        matrix.append(row)    
    return matrix   

create(m,n) 

print('Normal')
for i in range(m):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()    

for i in range(m):
    for j in range(n):
        if matrix[i][j] =='o':
            matrix[i][j] = 'x'
        elif matrix[i][j] == 'x':
            matrix[i][j] = 'o'

print("Reverses")
for i in range(m):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()    
