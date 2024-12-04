def count_xmas_occurrences(grid, word="XMAS"):
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
            directions = [
                (0, 1),  # right
                (0, -1),  # left
                (1, 0),  # down
                (-1, 0),  # up
                (1, 1),  # diagonal down-right
                (1, -1),  # diagonal down-left
                (-1, 1),  # diagonal up-right
                (-1, -1),  # diagonal up-left
            ]
            for dx, dy in directions:
                if search(x, y, dx, dy):
                    count += 1

    return count

with open('day4/input.txt', 'r') as file:
    data = file.read().strip()
# Example grid
# grid = [
#     "MMMSXXMASM",
#     "MSAMXMSMSA",
#     "AMXSXMAAMM",
#     "MSAMASMSMX",
#     "XMASAMXAMM",
#     "XXAMMXXAMA",
#     "SMSMSASXSS",
#     "SAXAMASAAA",
#     "MAMMMXMMMM",
#     "MXMXAXMASX",
# ]
grid = data.split("\n")
# Count occurrences of "XMAS"
result = count_xmas_occurrences(grid)
print(f"Total 'XMAS' occurrences: {result}")
