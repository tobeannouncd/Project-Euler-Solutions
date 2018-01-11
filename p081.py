# -*- coding: utf-8 -*-
"""
@author: tobeannouncd

Project Euler

Problem 81: Path sum: Two ways
"""
from time import clock

# =============================================================================
# def mat_to_tree(mat):
#     tree = []
#     size = len(mat)
#     if size == 1:
#         return mat
#     
# #    top half
#     for i in range(size):
#         tree.append([])
#         for j in range(i + 1):
#             tree[-1].append(mat[i - j][j])
#             
# #    bottom half
#     for j in range(1, size):
#         tree.append([])
#         for i in range(size - j):
#             tree[-1].append(mat[size - 1 - i][j + i])
#     
#     return tree
# =============================================================================

start_time = clock()

with open('p081_matrix.txt') as f:
    mat = [[int(c) for c in line.strip().split(',')] for line in f.readlines()]

#tree = mat_to_tree(mat)

i_size, j_size = len(mat), len(mat[0])

for i in range(i_size):
    for j in range(j_size):
        mat[i][j] += min(mat[i-1][j], mat[i][j-1]) if i*j > 0 else \
            (mat[i-1][j] if i else (mat[i][j-1] if j else 0))
        
print(mat[-1][-1])

time_elapsed = clock() - start_time
print('Executed in {:.3G} seconds.'.format(time_elapsed))