#  \lessons\8-leader\dominator.py
# URL: https://app.codility.com/programmers/lessons/8-leader/dominator/

# My solution URL: https://app.codility.com/demo/results/training2PW4GZ-2G4/

"""
An array A consisting of N integers is given. The dominator of array A is the value
that occurs in more than half of the elements of A.

For example, consider array A such that
 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3

The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in
those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

Write a function

    `def solution(A)`

that, given an array A consisting of N integers, returns index of any element of
array A in which the dominator of A occurs. The function should return −1 if array A
does not have a dominator.

For example, given array A such that
 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3

the function may return 0, 2, 4, 6 or 7, as explained above.

Write an efficient algorithm for the following assumptions:

    * N is an integer within the range [0..100,000];
    * each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
"""

a = [3, 4, 3, 2, 3, -1, 3, 3]


# Attempt 2
def solution(A: list) -> int:
    length = len(A)
    if length == 0:
        return -1    
    half_len = length // 2
    leader = -1

    # Create new variable for sorted array.
    Arr = sorted(A)

    # Result must occupy at least half of the array.
    curr_item = Arr[half_len]

    count = 0
    for i in range(length):
        if Arr[i] == curr_item:
            count += 1
    if count > half_len:
        leader = curr_item
    if leader > 0:
        return A.index(leader)
    else:
        return leader

    return -1


# # Attempt 1
# def solution(A: list) -> int:
#     half_len = len(A) // 2
#     for itm in A:
#         if A.count(itm) > half_len:
#             return A.index(itm)
#     return -1
