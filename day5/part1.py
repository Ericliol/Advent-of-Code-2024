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

def find_middle_number(update):
    """Finds the middle number in an update."""
    return update[len(update) // 2]

def calculate_middle_sum(input_data):
    """Calculates the sum of middle numbers of correctly ordered updates."""
    rules, updates = parse_input(input_data)
    middle_numbers = []
    
    for update in updates:
        if is_correct_order(update, rules):
            middle_numbers.append(find_middle_number(update))
    
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
result = calculate_middle_sum(input_data)
print(f"The sum of the middle page numbers of correctly ordered updates is: {result}")
