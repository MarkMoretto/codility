
# https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/

"""
You are given N counters, initially set to 0, and you have two possible operations on them:

* increase(X) − counter X is increased by 1,
* max counter − all counters are set to the maximum value of any counter.


A non-empty array A of M integers is given. This array represents consecutive operations:

* if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
* if A[K] = N + 1 then operation K is max counter.


For example, given integer N = 5 and array A such that:
    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4

the values of the counters after each consecutive operation will be:
    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)

The goal is to calculate the value of every counter after all operations.

Write a function:

    def solution(N, A)

that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.

For example, given:
    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4

the function should return [3, 2, 2, 4, 2], as explained above.

Write an efficient algorithm for the following assumptions:
* N and M are integers within the range [1..100,000];
* each element of array A is an integer within the range [1..N + 1].
"""



N = 5
A = [3,4,4,6,1,4,4]
target = N + 1

a = [0] * N
max_n = [0]

def f(arr):
    if arr:
        el, arr = arr[0], arr[1:]
        idx = el - 1
        if 1 <= el <= N:
            a[idx] = a[idx] + 1
            if a[idx] > max_n[0]:
                max_n[0] = a[idx]
        if el == target:
            a[:] = [max_n[0] for _ in range(N)]
        return f(arr)
    

# f(A)



    
hashlist = lambda q: "".join(map(str, q))
dumb_memo = {}
def solution(N, A):
    hashid = hashlist(A)
    if hashid in dumb_memo:
        return dumb_memo[hashid]
    TRGT = N + 1
    a = [0] * N
    max_n = [0]

    for el in A:
        idx = el - 1
        if el == TRGT:
            a[:] = [max_n[0] for _ in range(N)]

        elif 1 <= el <= N:
            a[idx] = a[idx] + 1
            if a[idx] > max_n[0]:
                max_n[0] = a[idx]

    dumb_memo[hashid] = a
    return dumb_memo[hashid]




# for i in A:
#     if i == target:
#         a = [max(a)] * N
#     else:
#         a[i-1] += 1
#     print(a)



# def solution(N, A):
#     a = [0] * N
#     max_n = [0]
#     for i in A:
#         if 1 <= i <= N:
#             if max_n > a[i-1]:
#                 a[i-1] = max_n
        
#         max_n = max(a)
#         if i == N + 1:
#             a[:] = [max_n for _ in range(N)]
#         else:
#             a[i-1] = a[i-1] + 1
        
#     return a

solution(N, A)

