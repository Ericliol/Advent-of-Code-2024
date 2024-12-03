import re

total = 0
mul_enabled = True 
with open('day3/input.txt', 'r') as file:
    data = file.read()
    # Regex to match valid mul(X,Y) instructions
mul_pattern = r'mul\((\d{1,3}),\s*(\d{1,3})\)'
do_pattern = r'do\(\)'
dont_pattern = r"don't\(\)"
# data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

control_matches = re.findall(f'{do_pattern}|{dont_pattern}', data)

# Iterate through each match in the order of appearance
instructions = re.findall(f'{mul_pattern}|{do_pattern}|{dont_pattern}', data)
print(instructions)
print(control_matches)

i = 0
for match in instructions:
    if match[0] and match[1]:  # Valid mul instruction
        if mul_enabled:
            x, y = int(match[0]), int(match[1])
            total += x * y
    elif control_matches[i]  == "do()":  # Handle do()
        mul_enabled = True
        i+=1
    elif control_matches[i]  == "don't()":  # Handle don't()
        mul_enabled = False
        i+=1
    
print(total)