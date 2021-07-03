
from typing import List


v = lambda A, S, N: abs(sum([A[i] * S[i] for i in range(N)]))


a: List[int] = [1, 5, 2, -2]
s: List[int] = [-1, 1, -1, 1]

print("\n".join([f"{i} {j+1}" for i in range(len(a)) for j in range(len(a)) if i < j+1]))

def solution(A: List[int] = None) -> int:
    if A is None:
        return 0
    