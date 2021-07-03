
"""
Purpose: 
Date created: 2020-05-16

Contributor(s):
    Mark M.

Description:

    There are N rectangular buildings standing along the road next to each other. The
    K-th building is of size H[K] × 1.
    
    Because a renovation of all of the buildings is planned, we want to cover them with
    rectangular banners until the renovations are finished. Of course, to cover a building,
    the banner has to be at least as high as the building. We can cover more than one
    building with a banner if it is wider than 1.
    
    For example, to cover buildings of heights 3, 1, 4 we could use a banner of size 4×3
    (i.e. of height 4 and width 3), marked here in blue:
    
    Buildings of sizes (3 × 1), (1 × 1), (4 × 1), covered with scaffolding of size 4×3
    
    We can order at most two banners and we want to cover all of the buildings. Also, we
    want to minimize the amount of material needed to produce the banners.
    
    What is the minimum total area of at most two banners which cover all of the
    buildings?
"""

N = 2 # Number of banners




def solution(H):
    max_h = max(H)
    max_h_idx = [i for i, v in enumerate(H) if v == max_h]
    if len(max_h_idx) == 1:
        max_idx = max_h_idx[0]
        if max_idx != 0 and max_idx != len(H) - 1:
            if H[:max_idx] < H[max_idx+1:]:
                max_h_idx = [max_idx, len(H) - 1]
            else:
                max_h_idx = [0, max_idx]
    
    max_h_rng = [i for i in range(min(max_h_idx), max(max_h_idx)+1)]
    max_h_sum = sum([max_h for i in max_h_rng])
    
    # Remove max
    rem_h = [i for i in H if not H.index(i) in max_h_rng]
    rem_h_sum = 0
    if len(rem_h) > 0:
        rem_h_sum = max(rem_h) * len(rem_h)
    result = max_h_sum + rem_h_sum
    return result






### Tests
def tests():
    H = [3,1,4]
    assert (solution(H) == 10), f"Failed test for {H}"
    
    
    H = [5, 3, 2, 4]
    assert (solution(H) == 17), f"Failed test for {H}"
    
    
    H = [1, 1, 7, 6, 6, 6]
    assert (solution(H) == 30), f"Failed test for {H}"
    
    
    H =  [7, 7, 3, 7, 7] # Error
    assert (solution(H) == 35), f"Failed test for {H}"
    
    
    H =  [7] # Error
    assert (solution(H) == 7), f"Failed test for {H}"


two_heights = H = [1,1,1,7,1,7,]
solution(H)

sample_err = H = [7, 8, 4, 6, 2, 10, 1, 3, 5, 9] # Expected 90, got 96
solution(H)

"""
-- Correctness tests
two_heights
There are at most two different heights of buildings. N<=10.

WRONG ANSWER
got 90000 expected 90001


permutation
The list is a permutation of numbers [1, N]. N<=50.
WRONG ANSWER
got 96 expected 90



random_small
A random array. N=50.
WRONG ANSWER
got 4771 expected 4730


random_medium
A random array. N=500.
WRONG ANSWER
got 4908922 expected 4963485


-- Performance
distinct_large
Every value in the array is different. N=7,500.
TIMEOUT ERROR
running time: 0.836 sec., time limit: 0.208 sec.

random_max
Random maximum tests. N=100,000.
TIMEOUT ERROR
Killed. Hard limit reached: 6.000 sec.

various_max
Various hard hand-created tests. N=100,000.
TIMEOUT ERROR
Killed. Hard limit reached: 6.000 sec.


max_pyramid
Values in the tests are arranged into ascending or descending pyramids. N=100,000.
TIMEOUT ERROR
Killed. Hard limit reached: 6.000 sec.


max
No additional constraints.
TIMEOUT ERROR
Killed. Hard limit reached: 7.000 sec.

"""
