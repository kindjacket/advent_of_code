### read in input
from itertools import combinations

lines = [int(i) for i in open("input.txt").read().splitlines()]

target_sum = 2020
for (i, a), (j, b) in combinations(enumerate(lines), 2):
    if a + b == target_sum:
        print(a * b)
        break
