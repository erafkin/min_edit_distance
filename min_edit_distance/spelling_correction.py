# Emma Rafkin
# CS72 Homework 1
# April 2019


import numpy as np
import sys
insert_cost = 1.0
delete_cost = 2.0
substitution_cost = 3.0
twiddle_cost = 5.0

def insert(char):
    if(is_common_double(char)):
        return (insert_cost/2)
    return insert_cost

def delete(char):
    return delete_cost

def substitute(char1, char2):
    if(char1 == char2):
        return 0.0
    elif(is_vowel(char1) & is_vowel(char2)):
        #lower swap cost if they are both vowels
        return (substitution_cost/2)
    elif(usual_swap(char1, char2)):
        #lower swap cost if it is a usual swap
       return (substitution_cost/2)
    else:
        return substitution_cost

def twiddle(char1_1, char1_2, char2_1, char2_2):
    if ((char1_1 == char2_2) & (char2_1 == char1_2)):
            return 0.0
    elif common_twiddle(char2_1, char2_2):
        return insert_cost/2
    return twiddle_cost

def is_common_double(c):
    #most commonly repeated letters in english: ss, ee, tt, ff, ll, mm and oo.
    letters = ['s', 'e', 't', 'f', 'l', 'm', 'o']
    if (c in letters):
        return True
    return False

def common_twiddle(c1, c2):
    swaps = {'h':'t','e': 'i','a': 'e','w':'o'}
    if (c1 in list(swaps.keys())):
        if (c2 == swaps.get(c1)):
            return True
    return False

def usual_swap(c1, c2):
    #commonly swapped out letters
    swaps = [['c', 's'], ['m','n']]
    for swap in swaps:
        if (c1 in swap):
            if(c2 in swap):
                return True
    return False

def is_vowel(c):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if (c in vowels):
        return True
    return False

def med(str1, str2):
    n = len(str1)
    m = len(str2)
    d = np.zeros((n+1, m+1))
    #initialize bottom corner
    d[0][0] = 0
    #initialize the first row and column to 0
    for r in range(1, n+1):
        d[r][0] = d[r-1][0] + insert_cost
    for c in range(1, m+1):
        d[0][c] = d[0][c-1] + delete_cost

    for i in range(1, n+1):
        for j in range(1, m+1):
            curr = min(d[i - 1][j] + insert(str1[i - 1]), d[i - 1][j - 1] + substitute(str1[i - 1], str2[j - 1]), d[i][j - 1] + delete(str2[j - 1]))
            if i > 1:
                if j > 1:
                    curr = min(curr, d[i - 2][j - 2]+twiddle(str1[i-2l], str1[i-1], str2[j-2], str2[j-1]))
            d[i][j] = curr
    return d[n][m]

def correct_spelling(m, d, of):
    for source in m:
        lowest_med = 10000000
        correction_options = []
        for target in d:
            min_ed = med(target, source)
            if min_ed == lowest_med:
                correction_options.append(target)
            if min_ed < lowest_med:
                lowest_med = min_ed
                del correction_options[:]
                correction_options.append(target)
        print(source, correction_options[-1])
        of.write(correction_options[-1])

dict = open(sys.argv[1])
d = dict.readlines()

ms = open(sys.argv[2])
m = ms.readlines()

output_file = open("spelling_corrections_output.txt", "w")
correct_spelling(m, d, output_file)

dict.close()
ms.close()
output_file.close()

