from itertools import product

def evaluate_expression_with_concat(numbers, operators):
    """Evaluates the expression with given numbers and operators left-to-right, including concatenation."""
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        elif op == '||':
            result = int(str(result) + str(numbers[i + 1]))
    return result

def parse_input(input_text):
    """Parses the input text and returns a list of equations."""
    equations = []
    for line in input_text.strip().split("\n"):
        test_value, numbers = line.split(":")
        test_value = int(test_value)
        numbers = list(map(int, numbers.split()))
        equations.append((test_value, numbers))
    return equations

def calculate_calibration_with_concat(input_text):
    """Calculates the total calibration result including concatenation."""
    equations = parse_input(input_text)
    total_calibration = 0

    for test_value, numbers in equations:
        n = len(numbers)
        possible = False

        # Generate all combinations of operators
        for operators in product(["+", "*", "||"], repeat=n-1):
            if evaluate_expression_with_concat(numbers, operators) == test_value:
                possible = True
                break

        if possible:
            total_calibration += test_value

    return total_calibration

# Example Input
input_text = """\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""
with open('day7/input.txt', 'r') as file:
    input_text = file.read().strip()
# Calculate the total calibration result
result = calculate_calibration_with_concat(input_text)
print(f"The total calibration result is {result}.")
