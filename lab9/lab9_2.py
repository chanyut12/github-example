n = int(input())

a_inverse = [[0 for j in range(n)] for i in range(n)]
#print(a_inverse)

matrix = []

def create(n):
    for i in range(n):
        row = []
        for j in range(n):
            col = int(input())
            row.append(col)
        matrix.append(row)   
    return matrix     

create(n)

for i in range(n):
    for j in range(n):
        a_inverse[j][i] = matrix[i][j]
#print(a_inverse)

# print("Matrix A")
# print([[matrix[i][j] for i in range(n)] for j in  range(n)])

# print("Matrix A Transpose")
# print(print([[a[i][j] for i in range(n)] for j in range(n)]))

print("Matrix A")
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()



print("Matrix A Transpose")
for i in range(n):
    for j in range(n):
        print(a_inverse[i][j], end=' ')      
    print()     

