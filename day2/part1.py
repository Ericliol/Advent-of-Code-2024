def is_safe_report(report):
    # Check if all differences are between 1 and 3
    for i in range(1, len(report)):
        diff = abs(report[i] - report[i - 1])
        if diff < 1 or diff > 3:
            return False

    # Check if the list is either strictly increasing or decreasing
    increasing = all(report[i] > report[i - 1] for i in range(1, len(report)))
    decreasing = all(report[i] < report[i - 1] for i in range(1, len(report)))

    return increasing or decreasing

def count_safe_reports(reports):
    return sum(1 for report in reports if is_safe_report(report))

def convert_input_to_matrix(input_text):
    # Split the input into lines and then each line into individual integers
    matrix = [list(map(int, line.split())) for line in input_text.strip().split('\n')]
    return matrix

with open('day2/input.txt', 'r') as file:
    # Read the file line by line and convert each line to a list of integers
    matrix = [list(map(int, line.split())) for line in file]

safe_count = count_safe_reports(matrix)
print(safe_count)
    