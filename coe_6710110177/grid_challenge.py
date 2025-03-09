def gridChallenge(grid):
    sorted_rows = [''.join(sorted(row)) for row in grid]
    
    n = len(sorted_rows)
    for col in range(len(sorted_rows[0])):
        for row in range(1, n):
            if sorted_rows[row][col] < sorted_rows[row - 1][col]:
                return "NO"
    return "YES"
