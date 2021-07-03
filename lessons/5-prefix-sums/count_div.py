# ~\lessons\5-prefix-sums\count_div.py

# https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/


modeval = lambda n, m: (n % m) == 0

def solution(A, B, K):
    if A == B:
        return 1 if modeval(A, K) else 0
    return round(((B + 1) - A) / K)
    # return sum([1 for i in range(A, B, K)])


solution(6, 11, 2) # 3
solution(0, 0, 11) # 1
solution(1, 1, 11) # 0
solution(11, 345, 17) # 20
solution(100, 123_000_000, 2) # 61499950
solution(101, 123_000_000, 10000)
solution(0, 2_000_000_000, 1) # 2000000001
solution(0, 2_000_000_000, 2_000_000_000) # 2
solution(2_000_000_000, 2_000_000_000, 2_000_000_000) # 1
solution(0, 0, 1) # 1
solution(2_000_000_000, 2_000_000_000, 1) # 1
solution(10, 10, 5)
solution(10, 10, 7)
solution(10, 10, 20)
solution(0, 1, 11)
solution(1, 1, 11)