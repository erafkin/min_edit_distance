# Minimum Edit Distance
## Overview
Originally used levenshtein distance to calculate the minimum edit distance between words. Later shifted the cost for different changes in the words, which increased accuracy with possible overfitting. Effectively creates a spell check for dict.txt with 82% accuracy.
For more information on minimum edit distance, see [here](https://en.wikipedia.org/wiki/Edit_distance)
For my dynamic programming solution to the Minimum Edit Distance problem as laid out in CLRS, see [here](http://tiny.cc/med_rafkin_dorgan). Note that this solution was created with [Grace Dorgan](https://github.com/gracedorgan)

## Use
Clone the repository. Then in the terminal enter `python spelling_correction.py dict.txt misspellings.txt`

## Dev
Developed in python 2.7 for the Dartmouth class CS72 (Accelerated Computational Linguistics)
