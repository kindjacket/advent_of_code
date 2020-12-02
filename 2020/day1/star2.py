from itertools import combinations

lines = [int(i) for i in open("input.txt").read().splitlines()]

target_sum = 2020
for (i, a), (j, b), (k, c) in combinations(enumerate(lines), 3):
    if a + b + c == target_sum:
        print(a * b * c)
        break
