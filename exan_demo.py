
"""
Purpose: Demo exam
Date created: 2020-05-16

Contributor(s):
    Mark M.
"""


A = [1, 3, 6, 4, 1, 2]
a_min, a_max = min(A), max(A)
rng = set(range(a_min, a_max))
res = rng.difference(set(A))

def solution(A):

    a_set = set(A)
    n_set = set()
    i = min([i if i > 0 else 0 for i in a_set])
    if i <= 0:
        return 1
    else:
        i = 1
        while True:
            n_set.add(i)
            tmp = n_set.difference(a_set)
            if tmp.__len__() == 1:
                res = tmp.pop()
                if res > 0:
                    return res
                    break
            i += 1


solution([1,2,3])
solution([-1, -3])
solution([1, 3, 6, 4, 1, 2])
"""