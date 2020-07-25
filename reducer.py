#!/usr/bin/env python3

# importing modules
import sys
import pandas as pd
import numpy as np
import string
from scipy.spatial import distance


clusters_file = open('n_clusters.txt', 'r')
clusters_line = clusters_file.readlines()
clusters_file.close()
n_centroids = int(clusters_line[0].strip())
# print(n_centroids)

# reading feature vector length
for line in sys.stdin:
    vector_length = int(line.strip())
    break

# # creating random centroids
# centroids = []
# for i in range(n_centroids):
#     temp_centroid = np.random.randint(0, 10, size=vector_length)
#     centroids.append(temp_centroid)
# # print(np.array(centroids))

# loading vocab_file
centroids = []
centroids_file = open('centroids.txt', 'r')
centroids_lines = centroids_file.readlines()
centroids_file.close()
# removing '\n'
for index in range(n_centroids):
    centroids_lines[index] = centroids_lines[index].strip()
    centroids.append(list(map(int, centroids_lines[index].split())))
    # print(centroids[index])


distances = n_centroids * [0]
letters = list(string.ascii_uppercase)
categories = letters.copy()[:n_centroids]
# print(*categories)
categories_count = len(categories) * [0]
my_array = []
counter = 0
for line in sys.stdin:
    line = line.strip()
    line = list(map(int, line.split()))
    # my_array.append(line)
    for i in range(n_centroids):
        # distances[i] = np.linalg.norm(centroids[i] - line)
        distances[i] = distance.euclidean(centroids[i], line)
    min_idx = distances.index(min(distances))
    categories_count[min_idx] += 1
    # print(f'{counter}:\t', end='')
    # print(*categories_count, sep=' ')
    # print(f'The min distance of line {counter}: {min(distances)}\t\t\t\t\t\t\t{categories[min_idx]}')
    # print(f'{counter}:\t\t\t\t{categories[min_idx]}')
    centroids[min_idx] = np.array((np.array(centroids[min_idx]) + np.array(line)) / 2.0)
    counter += 1

# for line in sys.stdin:
#     line = line.strip()
#     line = list(map(int, line.split()))
#     print(f'==> Line: {line}')
#     for i in range(n_centroids):
#         distances[i] = np.linalg.norm(centroids[i] - line)
#         min_idx = distances.index(min(distances))
#     print(f'==> Cent{min_idx}: {centroids[min_idx]}')
#     print(f'==> Dest{min_idx}: {distances[min_idx]}')
    
#     centroids[min_idx] = list((np.array(centroids[min_idx]) + np.array(line)) / 2.0)
#     print(f'==> New{min_idx}: {centroids[min_idx]}')
#     # print(f'==> Cent1: {min(distances)} \t\t {categories[min_idx]}')
#     break

# print(f'==> Cent1: {line}')

# print(my_array)
# print(np.array(my_array))
# print('End successfully!')
print(*categories)
print(*categories_count, sep=' ')
# from sklearn.cluster import KMeans
# from sklearn.preprocessing import StandardScaler
# k_model = KMeans(n_clusters=3)

# scaled_features = StandardScaler().fit_transform(np.array(my_array))

# k_model = k_model.fit(scaled_features)
# print(k_model.labels_)
