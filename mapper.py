#!/usr/bin/env python3

# importing modules
import sys
import pandas as pd
import numpy as np

# reading main data
counter = 0
main_data = [0, 0, 0]
for line in sys.stdin:
    # remove white space
    line = line.strip()
    main_data[counter] = int(line)
    counter += 1
    if counter == 3:
        break

# collecting main data
n_docs = main_data[0]
n_words = main_data[1]
n_lines = main_data[2]
print(n_words)
# reading the rest of data and mapping into vectors
data_array = np.zeros((n_words), dtype=int)
article_idx = 0
# counter = 0
for line in sys.stdin:
    line = line.strip()
    line_data = list(map(int, line.split()))
    current_idx = line_data[0]
    if current_idx != article_idx:
        # distance = np.linalg.norm(cent1 - data_array)
        # print(f'Article {current_idx} has been vectorized! ==>\t distance: {distance}')
        print(*data_array, sep=' ')
        data_array = np.zeros((n_words), dtype=int)
        article_idx = current_idx
        # counter += 1
    data_array[line_data[1]] = line_data[2]

    # if counter == 28:
    #     break
print(*data_array, sep=' ')