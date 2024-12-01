with open('day 1/input.txt', 'r') as file:
    column1 = []
    column2 = []
    
    # Iterate over each line in the file
    for line in file:
        # Split each line into two parts
        num1, num2 = map(int, line.split())
        # Append numbers to respective arrays
        column1.append(num1)
        column2.append(num2)
        
    column1.sort()
    column2.sort()
    acc = 0
    for i, c1 in enumerate(column1):
        print(c1)
        rep = column2.count(c1)
        acc += rep*c1
    print(acc)
        