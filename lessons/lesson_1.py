
"""
Purpose: Codility lessons
Date created: 2020-05-16

Lesson 1: BinaryGap
URL: https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

Contributor(s):
    Mark M.

Challenge:

    A binary gap within a positive integer N is any maximal sequence of consecutive
    zeros that is surrounded by ones at both ends in the binary representation of N.
    For example, number 9 has binary representation 1001 and contains a binary gap
    of length 2. The number 529 has binary representation 1000010001 and contains
    two binary gaps: one of length 4 and one of length 3. The number 20 has binary
    representation 10100 and contains one binary gap of length 1. The number 15 has
    binary representation 1111 and has no binary gaps. The number 32 has binary
    representation 100000 and has no binary gaps.
    
    Write a function:
    
        def solution(N)
    
    that, given a positive integer N, returns the length of its longest
    binary gap. The function should return 0 if N doesn't contain a binary gap.
    
    For example, given N = 1041 the function should return 5, because N has binary
    representation 10000010001 and so its longest binary gap is of length 5. Given N
    = 32 the function should return 0, because N has binary representation '100000'
    and thus no binary gaps.
    
    Write an efficient algorithm for the following assumptions:
    
            N is an integer within the range [1..2,147,483,647].
"""

import textwrap as tw
desc = """
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

    def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..2,147,483,647].
""".strip()

print(tw.fill(text=desc, width=80, expand_tabs=False, tabsize=4,
              replace_whitespace=False, drop_whitespace=False))



rng = range(1, 2147483647)


a = bin(32).split("b")[1]
b = bin(1041).split("b")[1]

def solution(N):
    binary = bin(N).split("b")[1]
    i = 0
    ones = 0
    zeroes = 0
    max_n = 0
    while i < len(binary):
        if binary[i] == '1':
            ones += 1
            if zeroes > max_n:
                max_n = zeroes
            zeroes = 0
        else:
            zeroes += 1
        i += 1
    return max_n

solution(9) # 2
solution(529) # 4
solution(20) # 1

solution(32)

solution(1041)





















