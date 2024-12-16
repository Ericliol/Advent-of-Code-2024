from collections import defaultdict
from functools import lru_cache
import math

def split_stone(number):
    """
    Splits a number into two stones if it has an even number of digits.
    Returns the left and right parts as integers.
    """
    digits = math.floor(math.log10(number)) + 1
    mid = digits // 2
    left = number // 10**mid
    right = number % 10**mid
    return left, right

def p2_helper(value, remaining, lookup):
    """
    Maps a value and a number of blinks remaining to the number of stones in the result.
    Base case: no blinks remaining ==> one stone.
    Uses memoization to avoid redundant calculations.
    """
    # print(value, remaining,lookup)
    if remaining == 0:
        return 1

    if (value, remaining) in lookup:
        return lookup[(value, remaining)]

    if value == 0:
        result = p2_helper(1, remaining - 1, lookup)
    elif len(str(value)) % 2 == 0:
        left, right = split_stone(value)
        result = p2_helper(left, remaining - 1, lookup) + p2_helper(right, remaining - 1, lookup)
    else:
        result = p2_helper(value * 2024, remaining - 1, lookup)
    
    lookup[(value, remaining)] = result
    return result

def part_2(infile, blink_total):
    """
    Calculates the total number of stones after the specified number of blinks.
    Optimized using memoization to handle large numbers of blinks efficiently.
    """
    lookup = {}
    stones = infile
    return sum(p2_helper(stone, blink_total, lookup) for stone in stones)

def part_1(infile, blink_total):
    """
    Simulates the transformation of stones over the specified number of blinks.
    Implements direct simulation without memoization.
    """
    stones = infile

    for blinks in range(1, blink_total + 1):
        i = 0
        while i < len(stones):
            n = stones[i]
            if n == 0:
                stones[i] = 1
            elif len(str(n)) % 2 == 0:
                digits = (math.floor(math.log10(n)) + 1) // 2
                left = n // 10**digits
                right = n % 10**digits
                stones[i] = left
                stones.insert(i + 1, right)
                i += 1
            else:
                stones[i] *= 2024
            i += 1

        if blinks <= 6:
            print(f"{blinks}:	{stones}")
        elif blinks >= 30 and blinks % 5 == 0:
            print(blinks)

    return len(stones)

# Read input from file
with open('day11/input.txt', 'r') as file:
    initial_stones = list(map(int, file.read().strip().split(' ')))

# initial_stones = [125,17]
# Number of blinks
num_blinks = 25

print("Part 1:", part_1(initial_stones, 25))
print("Part 2:", part_2(initial_stones, 75))