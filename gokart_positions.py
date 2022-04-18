import numpy as np
import pandas as pd
import sys
import itertools as it
import math

# Execution (provided that there is 5040 permutations to combine): 
#   python gokart_positions.py 0 1259
#   python gokart_positions.py 1260 2519
#   python gokart_positions.py 2520 3779
#   python gokart_positions.py 3780 5039

# Based on example code at https://docs.python.org/3/library/itertools.html#itertools.permutations
# But, apparently this is much slower than itertools implementation...
# Added jump parameter to skip first jump permutations
def permutations(iterable, r=None, jump=0):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    if jump == 0:
        yield tuple(pool[i] for i in indices[:r])
    else:
        cycles[0] -= (jump - 1)
        for i in range(0, jump):
            indices[0], indices[i] = indices[i], indices[0]
    while n:
        iterations = reversed(range(r))
        if jump > 0:
            iterations = [0]
            jump = 0
        for i in iterations:
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

def is_unique_arr(all_perms):
    number_of_columns = len(all_perms[0])
    number_of_rows = len(all_perms)
    for i in range(0, number_of_columns): # Iterate over columns
        # Prepare empty array to record number of instances of each value
        duplicates = [0] * number_of_columns
        for j in range(0, number_of_rows): # Iterate over rows
            old_count = duplicates[all_perms[j][i] - 1]
            if old_count > 0:
                return False
            duplicates[all_perms[j][i] - 1] = old_count + 1
    return True

def calc_avgs(all_perms):
    perms_count = len(all_perms)
    perm_len = len(all_perms[0])
    avgs = []
    avg_min = sys.maxsize
    avg_max = -sys.maxsize
    for i in range(0, perm_len):
        sum = 0
        for j in range(0, perms_count):
            sum = sum + all_perms[j][i]
        avg = sum / perms_count
        avgs.append(avg)
        if avg < avg_min:
            avg_min = avg
        if avg > avg_max:
            avg_max = avg

    diff2 = avg_max - avg_min

    return (diff2, avgs, all_perms)

def calc(level, lastmaxmin, higher_perms):
    print(f"Level: {level} - {lastmaxmin} - {higher_perms}")

    perms = permutations(karts, jump=level-1)
    #perms = it.permutations(karts)
    i = 0
    for perm in perms:
        i = i + 1
        print(f"level {level}, count {i}", end='\r', flush=True) if i % 100000 == 0 else None

        all_perms = higher_perms + [perm]
        
        unique_arr = is_unique_arr(all_perms)
        if not unique_arr:
            continue

        if level < stints:
            # We did not reach required number of stints yet
            lastmaxmin = calc(level=level+1, lastmaxmin=lastmaxmin, higher_perms=all_perms)

        elif level == stints:
            # We have reached required number of stints
            # Now we need to check if we have a solution
            # that is better than the previous one
            (diff2, avgs, df) = calc_avgs(all_perms)
            if diff2 <= lastmaxmin and diff2 <= 1:
                lastmaxmin = diff2
                print() # newline
                print(diff2)
                print(df)
                print(avgs)

        else:
            print() # newline
            print(f"ERROR: level = {level}, we should not be here")

    return lastmaxmin

if __name__ == '__main__':

    karts = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    # karts = [1,2,3,4,5]
    number_of_karts = len(karts)

    stints = 6
    # stints = 3

    print(f"number of permutations = {math.factorial(number_of_karts)}")

    best_lastmaxmin = calc(level=1, lastmaxmin=number_of_karts, higher_perms=[])
    print() # newline
    print(f"best_lastmaxmin = {best_lastmaxmin}")
