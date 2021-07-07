# lessons\12-euclidean-algorithm\common_prime_divisors.py

# Solution URL:
#   

# https://app.codility.com/programmers/lessons/12-euclidean_algorithm/common_prime_divisors/

"""
A prime is a positive integer X that has exactly two distinct divisors: 1 and X.
The first few prime integers are 2, 3, 5, 7, 11 and 13.

A prime D is called a prime divisor of a positive integer P if there exists a positive
integer K such that D * K = P. For example, 2 and 5 are prime divisors of 20.

You are given two positive integers N and M. The goal is to check whether the sets of
prime divisors of integers N and M are exactly the same.

For example, given:

    * N = 15 and M = 75, the prime divisors are the same: {3, 5};
    * N = 10 and M = 30, the prime divisors aren't the same: {2, 5} is not equal to {2, 3, 5};
    * N = 9 and M = 5, the prime divisors aren't the same: {3} is not equal to {5}.

Write a function:

    `def solution(A, B)`

that, given two non-empty arrays A and B of Z integers, returns the number of positions K
for which the prime divisors of A[K] and B[K] are exactly the same.

For example, given:
    A[0] = 15   B[0] = 75
    A[1] = 10   B[1] = 30
    A[2] = 3    B[2] = 5

the function should return 1, because only one pair (15, 75) has the same set of prime divisors.

Write an efficient algorithm for the following assumptions:

    * Z is an integer within the range [1..6,000];
    * each element of arrays A, B is an integer within the range [1..2,147,483,647].
"""

a = [15, 10, 3]
b = [75, 30, 5]


def GCD(a, b):
    """Greatest common divisor."""
    rem = a % b
    if rem == 0:
        return b
    else:
        return GCD(b, rem)

def LCM(a, b):
    """Least Common Multiple."""    
    return (a * b) / GCD(a, b)

def divisor_count(n):
    i = 1
    res = 0
    while (i ** 2) < n:
        if (n % i) == 0:
            res += 2
        i += 1
    if (i ** 2) == n:
        res += 1
    return res

divisor_count(10)

def is_prime(n):
    if n >= 2:
        half_n = n // 2
        for i in range(2, half_n + 1):
            if n % i == 0:
                return False
        return True
    return True

for i in range(21): print(i, is_prime(i))


