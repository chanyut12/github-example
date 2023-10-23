# def compute_risk(row, col, infected_positions):
#     risk = 0  # risk initialization
    
#     for i, j in infected_positions:
#         distance = abs(row - i) + abs(col - j)
        
#         if distance == 0:
#             return 100
#         elif distance == 1:
#             risk = max(risk, 60)
#         elif distance == 2:
#             risk = max(risk, 20)
    
#     return risk

# def main():
#     m = int(input().strip())  # number of rows
#     n = int(input().strip())  # number of columns
#     current_row = int(input().strip())
#     current_col = int(input().strip())
#     num_infected = int(input().strip())
    
#     # Read the positions of the infected people
#     infected_positions = [tuple(map(int, input().split())) for _ in range(num_infected)]
    
#     safe_count = 0
#     for row in range(m):
#         for col in range(n):
#             if compute_risk(row, col, infected_positions) == 0:
#                 safe_count += 1
                
#     current_risk = compute_risk(current_row, current_col, infected_positions)
    
#     print(safe_count)
#     print(f"{current_risk}%")

# if __name__ == "__main__":
#     main()


def calculate_risk(m, n, i, j, infected_positions):
    grid = [[0 for _ in range(n)] for _ in range(m)]
    
    # Mark infection areas
    for x, y in infected_positions:
        grid[x][y] = 100
        # Risk 60%
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != 100:
                    grid[nx][ny] = max(grid[nx][ny], 60)
        # Risk 20%
        for dx in [-2, -1, 0, 1, 2]:
            for dy in [-2, -1, 0, 1, 2]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != 100 and grid[nx][ny] != 60:
                    grid[nx][ny] = max(grid[nx][ny], 20)

    # Count safe areas
    safe_areas = sum([row.count(0) for row in grid])

    return safe_areas, grid[i][j]

m = int(input())
n = int(input())
i = int(input())
j = int(input())

N = int(input())
infected_positions = [tuple(map(int, [input() for _ in range(2)])) for _ in range(N)]

safe, risk = calculate_risk(m, n, i, j, infected_positions)
print(safe)
print(f"{risk}%")
