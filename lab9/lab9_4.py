n = 3
a = [[0 for j in range(n)] for i in range(n)]
matrix = []

def create(n):
    for i in range(n):
        row = []
        for j in range(n):
            c = int(input())
            row.append(c)
        matrix.append(row)   
    return matrix

def check_rows(matrix):
    for i in range(len(matrix)):
        if matrix[i] == [matrix[i][0]] * 3:
            print(f"All {matrix[i][0]} on row {i}")

def check_columns(matrix):
    for j in range(3):
        col = [matrix[i][j] for i in range(3)]
        if col == [matrix[0][j]] * 3:
            print(f"All {matrix[0][j]} on column {j}")

def main():
    matrix = create(n)
    for row in matrix:
        print(" ".join(map(str, row)))   
    # print("____________________________________________")
    # for i in range(n):
    #     for j in range(n):
    #         print(matrix[i][j] , end=' ')
    #     print()    
    check_rows(matrix)
    check_columns(matrix)

if __name__ == "__main__":
    main()
  