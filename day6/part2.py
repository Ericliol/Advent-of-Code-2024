def parse_map(input_map):
    """Parses the input map and returns the grid, guard position, and initial direction."""
    grid = [list(row) for row in input_map.strip().split("\n")]
    directions = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}
    guard_pos = None
    guard_dir = None

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell in directions:
                guard_pos = (x, y)
                guard_dir = directions[cell]
                grid[y][x] = "."  # Replace guard symbol with open space
                break
        if guard_pos:
            break

    return grid, guard_pos, guard_dir, directions

def simulate_with_obstruction(grid, guard_pos, guard_dir, directions):
    """Simulates guard movement to check for loops."""
    visited = set()
    rows, cols = len(grid), len(grid[0])
    current_pos, current_dir = guard_pos, guard_dir

    while True:
        state = (current_pos, current_dir)
        if state in visited:
            return True  # Loop detected
        visited.add(state)

        next_pos = (current_pos[0] + current_dir[0], current_pos[1] + current_dir[1])

        if 0 <= next_pos[1] < rows and 0 <= next_pos[0] < cols and grid[next_pos[1]][next_pos[0]] == ".":
            current_pos = next_pos
        else:
            # Check if guard is exiting the mapped area
            next_pos = (current_pos[0] + current_dir[0], current_pos[1] + current_dir[1])
            if not (0 <= next_pos[1] < rows and 0 <= next_pos[0] < cols):
                break
            # Turn right (90 degrees clockwise)
            if current_dir == directions["^"]:
                current_dir = directions[">"]
            elif current_dir == directions[">"]:
                current_dir = directions["v"]
            elif current_dir == directions["v"]:
                current_dir = directions["<"]
            elif current_dir == directions["<"]:
                current_dir = directions["^"]

            

    return False  # No loop detected

def count_obstruction_positions(input_map):
    """Counts the number of positions where adding an obstruction creates a loop."""
    grid, guard_pos, guard_dir, directions = parse_map(input_map)
    rows, cols = len(grid), len(grid[0])
    loop_positions = 0

    for y in range(rows):
        for x in range(cols):
            if grid[y][x] == ".":  # Only consider empty positions
                # Temporarily add an obstruction
                grid[y][x] = "#"
                
                if simulate_with_obstruction(grid, guard_pos, guard_dir, directions):
                    
                    loop_positions += 1
                # Remove the obstruction
                grid[y][x] = "."

    return loop_positions

# Input map
input_map = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""
with open('day6/input.txt', 'r') as file:
    input_map = file.read().strip()

# Calculate the result
result = count_obstruction_positions(input_map)
print(f"There are {result} different positions where you could add an obstruction to create a loop.")
