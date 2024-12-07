def parse_input(input_data):
    """Parses the input data into rules and updates."""
    rules_section, updates_section = input_data.strip().split("\n\n")
    rules = [tuple(map(int, rule.split('|'))) for rule in rules_section.splitlines()]
    updates = [list(map(int, update.split(','))) for update in updates_section.splitlines()]
    return rules, updates

def is_correct_order(update, rules):
    """Checks if an update adheres to the rules."""
    for a, b in rules:
        if a in update and b in update:
            if update.index(a) > update.index(b):
                return False
    return True

def reorder_update(update, rules):
    """Reorders an update according to the rules."""
    # Build a graph from the rules
    from collections import defaultdict, deque

    graph = defaultdict(list)
    in_degree = defaultdict(int)
    pages = set(update)

    # Add only rules that involve pages in this update
    for a, b in rules:
        if a in pages and b in pages:
            graph[a].append(b)
            in_degree[b] += 1
            if a not in in_degree:
                in_degree[a] = 0

    # Perform topological sorting
    queue = deque([page for page in pages if in_degree[page] == 0])
    sorted_order = []

    while queue:
        current = queue.popleft()
        sorted_order.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_order

def find_middle_number(update):
    """Finds the middle number in an update."""
    return update[len(update) // 2]

def calculate_middle_sum_for_incorrect(input_data):
    """Finds the sum of middle numbers of reordered incorrect updates."""
    rules, updates = parse_input(input_data)
    incorrect_updates = []

    for update in updates:
        if not is_correct_order(update, rules):
            incorrect_updates.append(update)

    reordered_updates = [reorder_update(update, rules) for update in incorrect_updates]
    middle_numbers = [find_middle_number(update) for update in reordered_updates]

    return sum(middle_numbers)

# Example input
input_data = """\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""
with open('day5/input.txt', 'r') as file:
    input_data = file.read().strip()
# Calculate and print the result
result = calculate_middle_sum_for_incorrect(input_data)
print(f"The sum of the middle page numbers of reordered incorrect updates is: {result}")
