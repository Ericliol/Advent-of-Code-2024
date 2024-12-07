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
    # print(grid, guard_pos, guard_dir, directions)
    return grid, guard_pos, guard_dir, directions

def simulate_guard_path(grid, guard_pos, guard_dir, directions):
    """Simulates the guard's movement and returns the number of distinct visited positions."""
    visited = set()
    rows, cols = len(grid), len(grid[0])
    i = 0 
    while True:
        
        visited.add(guard_pos)
        next_pos = (guard_pos[0] + guard_dir[0], guard_pos[1] + guard_dir[1])
        print(guard_pos)
        i += 1
        # if i == 65:
        #     break

        # Check if the next position is out of bounds or blocked
        if (0 <= next_pos[1] < rows and 0 <= next_pos[0] < cols and grid[next_pos[1]][next_pos[0]] == "."):
            guard_pos = next_pos
        else:
            # Check if the guard has exited the mapped area
            next_pos = (guard_pos[0] + guard_dir[0], guard_pos[1] + guard_dir[1])
            if not (0 <= next_pos[1] < rows and 0 <= next_pos[0] < cols):
                break
            # Turn right (90 degrees clockwise)
            if guard_dir == directions["^"]:
                guard_dir = directions[">"]
            elif guard_dir == directions[">"]:
                guard_dir = directions["v"]
            elif guard_dir == directions["v"]:
                guard_dir = directions["<"]
            elif guard_dir == directions["<"]:
                guard_dir = directions["^"]

            

    return len(visited)

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

# Parse the input map
grid, guard_pos, guard_dir, directions = parse_map(input_map)

# Simulate the guard's path and get the result
distinct_positions = simulate_guard_path(grid, guard_pos, guard_dir, directions)
print(f"The guard will visit {distinct_positions} distinct positions.")
