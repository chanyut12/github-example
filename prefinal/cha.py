def flood_next_hour(n, m, grid):
    # คัดลอกแผนผังปัจจุบัน
    new_grid = [list(row) for row in grid]

    # ตรวจสอบแต่ละช่องว่ามีน้ำหรือไม่
    for i in range(n-1): # ไม่ต้องตรวจสอบแถวสุดท้าย เพราะน้ำไม่สามารถไหลลงไปยังแถวด้านล่างของมันได้
        for j in range(m):
            if grid[i][j] == '*':
                new_grid[i+1][j] = '*' # น้ำจะไหลลงมายังช่องด้านล่าง

    # แสดงผลลัพธ์
    for row in new_grid:
        print(' '.join(row))

# รับข้อมูลนำเข้า
n, m = map(int, input().split())
grid = [input().split() for _ in range(n)]

flood_next_hour(n, m, grid)

