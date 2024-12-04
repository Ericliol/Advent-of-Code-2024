def count_xmas_x_patterns(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Helper function to check if a specific pattern matches
    def matches_pattern(x, y, pattern):
        for dx, row_pattern in enumerate(pattern):
            for dy, char in enumerate(row_pattern):
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if char != '.' and grid[nx][ny] != char:
                        return False
                else:
                    return False
        return True

    # Define the two possible "X-MAS" patterns
    patterns = [
        ["M.S", ".A.", "M.S"],  # MAS forward
        ["S.M", ".A.", "S.M"],  # SAM reverse
    ]

    # Iterate over all possible starting points for 3x3 sections
    for x in range(rows - 2):  # Ensure space for 3 rows
        for y in range(cols - 2):  # Ensure space for 3 columns
            for pattern in patterns:
                if matches_pattern(x, y, pattern):
                    count += 1

    return count



# Given grid
grid = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX",
] 
grid = [
    "S.S.S.S.S.",
    ".A.A.A.A..",
    "M.M.M.M.M."
] 
# Count occurrences of "X-MAS" pattern
result = count_xmas_x_patterns(grid)
print(f"Total 'X-MAS' patterns: {result}")