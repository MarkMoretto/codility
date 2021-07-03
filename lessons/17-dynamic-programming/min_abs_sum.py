
from typing import List

N = 10
v = lambda A, S, N: abs(sum([A[i] * S[i] for i in range(N)]))


a: List[int] = [1, 5, 2, -2]

def solution(A: List[int] = None) -> int:
    if A is None:
        return 0
    