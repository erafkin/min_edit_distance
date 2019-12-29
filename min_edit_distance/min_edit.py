# Emma Rafkin
# CS72 Homework 1
# April 2019

import numpy as np
import sys

insert_cost = 1
delete_cost = 1
substitution_cost = 2

def insert(idx):
    return 1

def delete(idx):
    return 1
def substitute(idx1, idx2):
    if(idx1 == idx2):
        return 0
    else:
        return 2


def med(str1, str2):

    n = len(str1)
    m = len(str2)
    d = np.zeros((n+1, m+1));
    #initialize bottom corner
    d[0][0] =0
    #initialize the first row and column to 0

    for r in range(1, n+1):
        d[r][0] = d[r-1][0] + insert_cost
    for c in range(1, m+1):
        d[0][c] = d[0][c-1] + insert_cost

    for i in range(1, n+1):
        for j in range(1, m+1):
            d[i][j] = min(d[i-1][j] + insert(str1[i-1]), d[i-1][j-1] + substitute(str1[i-1], str2[j-1]), d[i][j-1] + delete(str2[j-1]))
    return d[n][m]

print(med(sys.argv[1], sys.argv[2]));


