import re

total = 0
with open('day3/input.txt', 'r') as file:
    data = file.read()
    # Regex to match valid mul(X,Y) instructions
mul_pattern = r'mul\((\d{1,3}),\s*(\d{1,3})\)'
# data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
# Find all matches in the data
matches = re.findall(mul_pattern, data)

# Iterate through matches and calculate the total
for x, y in matches:
    total += int(x) * int(y)
    
print(total)