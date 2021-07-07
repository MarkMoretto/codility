# lessons\12-euclidean-algorithm\chocolates_by_numbers.py

# Solution URL:
#   https://app.codility.com/demo/results/trainingF7X7TD-67Z/

# https://app.codility.com/programmers/lessons/12-euclidean_algorithm/chocolates_by_numbers/

"""
Two positive integers N and M are given. Integer N represents the number of chocolates arranged in a circle, numbered from 0 to N − 1.

You start to eat the chocolates. After eating a chocolate you leave only a wrapper.

You begin with eating chocolate number 0. Then you omit the next M − 1 chocolates or wrappers on the circle, and eat the following one.

More precisely, if you ate chocolate number X, then you will next eat the chocolate with number (X + M) modulo N (remainder of division).

You stop eating when you encounter an empty wrapper.

For example, given integers N = 10 and M = 4. You will eat the following chocolates: 0, 4, 8, 2, 6.

The goal is to count the number of chocolates that you will eat, following the above rules.

Write a function:

    def solution(N, M)

that, given two positive integers N and M, returns the number of chocolates that you will eat.

For example, given integers N = 10 and M = 4. the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

        N and M are integers within the range [1..1,000,000,000].
"""


n, m = 10, 4


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

# Attempt 1
def solution(N, M):
    # write your code in Python 3.6
    # pass
    return int(LCM(N, M) / M)

# # Attempt 1
# nextval = lambda X, N, M: (X + M) % N
# def solution(N, M):
#     # write your code in Python 3.6
#     # pass
#     total = 1
#     x_prev = 0
#     x = nextval(x_prev, N, M)
#     while x != 0:
#         x_prev = x
#         x = nextval(x_prev, N, M)
#         total += 1
#     return total


# For example, for the input (1, 1) the solution returned a wrong answer (got 0 expected 1). 