import numpy as np
import pandas as pd

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


num_of_karts = [1,2,3,4,5,6,7]
perms = permutation(num_of_karts)

lastmaxmin = len(num_of_karts)

for i in range(len(perms)):
    print(".")
    for j in range(len(perms)):
        # print("/")
        df = pd.DataFrame([
            perms[i],
            perms[j]
        ])
        if (not df[0].is_unique) or (not df[1].is_unique) or (not df[2].is_unique) or (not df[3].is_unique) or (not df[4].is_unique) or (not df[5].is_unique) or (not df[6].is_unique):
            continue
        
        for k in range(len(perms)):
            # print("=")
            df = pd.DataFrame([
                perms[i],
                perms[j],
                perms[k]
            ])
            if (not df[0].is_unique) or (not df[1].is_unique) or (not df[2].is_unique) or (not df[3].is_unique) or (not df[4].is_unique) or (not df[5].is_unique) or (not df[6].is_unique):
                continue
                
            for l in range(len(perms)):
                # Race is made of four runs
                df = pd.DataFrame([
                    perms[i],
                    perms[j],
                    perms[k],
                    perms[l]
                ])
                if (not df[0].is_unique) or (not df[1].is_unique) or (not df[2].is_unique) or (not df[3].is_unique) or (not df[4].is_unique) or (not df[5].is_unique) or (not df[6].is_unique):
                    continue

                # print(df)
                
                avgs = df.agg(['average'])

                avgs2 = avgs.agg('average')
                # firstavg = avgs.iat[0,0]
                # if avgs2 == firstavg:
                #     df
                #     avgs
                
                min2 = avgs.transpose().agg('min').iat[0]
                max2 = avgs.transpose().agg('max').iat[0]
                diff2 = max2 - min2
                if diff2 < lastmaxmin:
                    lastmaxmin = diff2
                    print(diff2)
                    print(df)
                    print(avgs)
