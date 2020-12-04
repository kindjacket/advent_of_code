from typing import List

from utils import get_input
from loguru import logger
import numpy as np

DAY = 3


def try_slope(input_data: List[List], step: np.array):
    visited_locations = [i * step for i in range(int(len(input_data)/step[1]))]
    tree_count = 0
    for i in visited_locations:
        x = i[0] % len(input_data[0])
        y = i[1]
        if input_data[y][x] == "#":
            tree_count += 1
    logger.info(f"{tree_count} trees encountered for route {step}")
    return tree_count


if __name__ == "__main__":
    input_data = [list(i) for i in get_input(DAY)]
    start = np.array([0, 0])
    input_width = len(input_data[0])
    step_options = [
        np.array([1, 1]),
        np.array([3, 1]),
        np.array([5, 1]),
        np.array([7, 1]),
        np.array([1, 2]),
    ]
    solution = np.product([try_slope(input_data, i) for i in step_options])
    logger.info(f"solution = {solution}")
