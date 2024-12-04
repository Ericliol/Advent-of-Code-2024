def count_xmas_occurrences(grid, word="MAS"):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    count = 0

    # Helper function to check a direction
    def search(x, y, dx, dy):
        for i in range(word_len):
            if not (0 <= x + i * dx < rows and 0 <= y + i * dy < cols):
                return False
            if grid[x + i * dx][y + i * dy] != word[i]:
                return False
        return True

    # Iterate through all grid positions
    for x in range(rows):
      for y in range(cols):
        # Check all 8 directions: right, left, down, up, and diagonals
        directions_right = [
          (1, 1),  # diagonal down-right
          (-1, 1),  # diagonal up-right
        ]
        directions_left = [
          (1, -1),  # diagonal down-left
          (-1, -1), # diagonal up-left
        ]
        i = 0 
        
        for dx, dy in directions_right:
          if search(x, y, dx, dy):
            for dx2, dy2 in directions_left:
              offx = dx - dx2
              offy = dy - dy2
              print(offx, offy)
              if search(x + offx, y + offy, dx, dy):
                count += 1
                
          i +=1
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
result = count_xmas_occurrences(grid)
print(f"Total 'X-MAS' patterns: {result}")