# trainings\5\disappearing_pairs.py

# Challenge URL: https://app.codility.com/programmers/trainings/5/disappearing_pairs/

# My latest solution URL: https://app.codility.com/demo/results/trainingPZ8SPM-HZE/

"""
A string S containing only the letters "A", "B" and "C" is given. The string can be transformed by removing one occurrence of "AA", "BB" or "CC".

Transformation of the string is the process of removing letters from it, based on the rules described above. As long as
at least one rule can be applied, the process should be repeated. If more than one rule can be used, any one of them could be chosen.

Write a function:

    `def solution(S)`

that, given a string S consisting of N characters, returns any string that can result from a sequence of transformations as described above.

For example, given string S = "ACCAABBC" the function may return "AC", because one of the possible sequences of transformations is as follows:

Also, given string S = "ABCBBCBA" the function may return "", because one possible sequence of transformations is:

Finally, for string S = "BABABA" the function must return "BABABA", because no rules can be applied to string S.

Write an efficient algorithm for the following assumptions:

* the length of S is within the range [0..50,000];
* string S consists only of the following characters: "A", "B" and/or "C".
"""

pairs: list  = ["AA", "BB", "CC"]


def has_pair(s: str, l: list) -> bool:
    return any([1 for p in l if p in s])

def split_join(s: str, token: str) -> str:
    return "".join(s.split(token))

def remover(s: str) -> str:
    while has_pair(s, pairs):
        for pair in pairs:
            s = split_join(s, pair)
    return s


def solution(S):
    return remover(S)




# --- Testing --- #

from typing import List
import secrets
letters: List[str] = ["A", "B", "C"]
pairs: List[str]  = list(map(lambda q: q * 2, letters))

def random_seq(length: int) -> str:
    return "".join([secrets.choice(letters) for _ in range(length)])

def random_pairs(n_pairs: int) -> str:
    return "".join([secrets.choice(pairs) for _ in range(n_pairs)])

def palindrome(length: int, odd: bool = True, pairs: bool = False) -> str:
    half_len = length // 2
    if pairs:
        lhs = "".join(random_pairs(half_len))
    else:
        lhs = "".join(random_seq(half_len))
    rhs = lhs[::-1]
    if odd:
        rhs = rhs[1:]
    return lhs + rhs


a: str = "ACCAABBC"
b: str = "ABCBBCBA"
c: str = "BABABA"
remover(a)
remover(b)
remover(c)

max_rand: str = random_seq(50000)
remover(max_rand)

max_pairs: str = random_seq(50000)
remover(max_pairs)

max_c: str = "C" * 50000
remover(max_c)

odd_palindrome = palindrome(50000, pairs = False)
remover(odd_palindrome)

big_palindrome1 = palindrome(50000, odd = False, pairs = False)
remover(big_palindrome1)

big_palindrome2 = palindrome(50000, odd = False, pairs = True)
remover(big_palindrome2)



# Attempt 3
# def remover(s: str) -> str:
#     while has_pair(s, pairs):
#         for pair in pairs:
#             s = s.replace(pair, "")
#     return s

# Attempt 2: Works, but hits recursion depth limit for larger
# def remover(string: str) -> str:
#     if len(string) > 1:
#         for pair in pairs:
#             if pair in string:
#                 string = string.replace(pair, "", 1)
#                 return remover(string)
#     return string


# Attempt 2
# def remover(S: str) -> str:
#     tmp: str = ""
#     print(S)
#     if not S:
#         return ""
#     if not has_pair(S, pairs):
#         return S
#     for pair in pairs:
#         tmp = S.replace(pair, "", 1)
#         S = tmp
#         break
#     return remover(S)