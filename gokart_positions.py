import numpy as np
import pandas as pd
import sys

# Execution (provided that there is 5040 permutations to combine): 
#   python gokart_positions.py 0 1259
#   python gokart_positions.py 1260 2519
#   python gokart_positions.py 2520 3779
#   python gokart_positions.py 3780 5039

# Python function to print permutations of a given list
def permutation(lst):

    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = [] # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list. remLst is
        # remaining list
        remLst = lst[:i] + lst[i+1:]

        # Generating all permutations where m is first
        # element
        for p in permutation(remLst):
            l.append([m] + p)
    return l

def is_unique(df):
    for i in range(len(df.columns)):
        if (not df[i].is_unique):
            return False
    return True

def calc(level, lastmaxmin, indexes):
    for i in range(len(perms)):
        print(f"level {level}, indexes {indexes + [i]}", end='\r', flush=True)

        df_input_array = []
        for idx in indexes:
            df_input_array.append(perms[idx])
        df_input_array.append(perms[i])
        
        df = pd.DataFrame(df_input_array)
        
        if not is_unique(df):
            continue

        if level < stints:
            # We did not reach required number of stints yet
            lastmaxmin = calc(level+1, lastmaxmin, indexes + [i])

        elif level == stints:
            # We have reached required number of stints
            # Now we need to check if we have a solution
            # that is better than the previous one
            avgs = df.agg(['average'])

            min2 = avgs.transpose().agg('min').iat[0]
            max2 = avgs.transpose().agg('max').iat[0]
            diff2 = max2 - min2
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


karts = [1,2,3,4,5,6,7]
perms = permutation(karts)

# lastmaxmin = len(karts)

stints = 4

print(f"number of permutations = {len(perms)}")

# lower = int(sys.argv[1])    
# upper = int(sys.argv[2])
# print(f"lower, upper = {lower},{upper}")

best_lastmaxmin = calc(1, len(karts), [])
print() # newline
print(f"best_lastmaxmin = {best_lastmaxmin}")

# for i in range(lower, upper):
#     print(".")
#     for j in range(len(perms)):
#         print("/")
#         df = pd.DataFrame([
#             perms[i],
#             perms[j]
#         ])
#         if not is_unique(df):
#             continue
        
#         for k in range(len(perms)):
#             print("=")
#             df = pd.DataFrame([
#                 perms[i],
#                 perms[j],
#                 perms[k]
#             ])
#             if not is_unique(df):
#                 continue
                
#             for l in range(len(perms)):
#                 # Race is made of four runs
#                 df = pd.DataFrame([
#                     perms[i],
#                     perms[j],
#                     perms[k],
#                     perms[l]
#                 ])
#                 if not is_unique(df):
#                     continue

#                 # print(df)
                
#                 avgs = df.agg(['average'])

#                 avgs2 = avgs.agg('average')
#                 # firstavg = avgs.iat[0,0]
#                 # if avgs2 == firstavg:
#                 #     df
#                 #     avgs
                
#                 min2 = avgs.transpose().agg('min').iat[0]
#                 max2 = avgs.transpose().agg('max').iat[0]
#                 diff2 = max2 - min2
#                 if diff2 <= lastmaxmin and diff2 <= 1:
#                     lastmaxmin = diff2
#                     print(diff2)
#                     print(df)
#                     print(avgs)
