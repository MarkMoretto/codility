# ~\lessons\5-prefix-sums\count_div.py

# https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/


# https://app.codility.com/demo/results/trainingEXHQKX-KV9/


# def GCD(a, b):
#     if b == 0:
#         return a
#     return GCD(b, a % b)
# def solution(A, B, K):
#     gcd_ = GCD(A, B)
#     return int((B - A) / K)

# modeval = lambda n, m: (n % m) == 0

def solution(A, B, K):
    add_on = 1 if A % K == 0 else 0
    return B//K - A//K + add_on

# def solution(A, B, K):
#     if A == B:
#         return 1 if modeval(A, K) else 0
#     return round(((B + 1) - A) / K)

# GCD(100, 123_000_000)
# GCD(101, 123_456_789)

solution(6, 11, 2) # 3
solution(0, 0, 11) # 1
solution(1, 1, 11) # 0
solution(11, 345, 17) # 20
solution(100, 123_000_000, 2) # 61499950
solution(101, 123_456_789, 10000) # 12345
solution(0, 2_000_000_000, 1) # 2000000001
solution(0, 2_000_000_000, 2_000_000_000) # 2
solution(2_000_000_000, 2_000_000_000, 2_000_000_000) # 1
solution(0, 0, 1) # 1
solution(2_000_000_000, 2_000_000_000, 1) # 1
solution(10, 10, 5) # 0
solution(10, 10, 7) # 1
solution(10, 10, 20) # 0
solution(0, 1, 11)
solution(1, 1, 11)
solution(1, 1, 1) # 1
solution(2_000_000_000, 2_000_000_000, 1) # 1




# # https://github.com/oxford-cs-deepnlp-2017/practical-1/blob/master/practical1.ipynb
# class SentenceItem:
#     lineno: int
#     tokens: list

# class SentenceToken(SentenceItem):

#     __slots__ = ["lineno", "tokens"]

#     def __init__(self, lineno, tokens):
#         self.lineno = lineno
#         self.tokens = tokens


# class SentenceCollection:
#     def __init__(self):
#         self.__items = []
#         self.__attrs = [i for i in dir(SentenceToken) if not i.startswith("_")]
        
#     def add(self, line_number, tokens):
#         self.__items.append(SentenceToken(line_number, tokens))
    
#     def delete(self, line_number):
#         for i in self.__items:
#             if i.lineno == line_number:
#                 self.__items.remove(i)
            
#     def items(self):
#         return [i for i in self.__items]


# # st_list = [
# #     SentenceToken(0, ["a", "b", "c"]),
# #     SentenceToken(1, ["f", "e", "d"]),
# # ] 
# st = SentenceToken(0, ["a", "b", "c"])
# attrs = [i for i in dir(SentenceToken) if not i.startswith("_")]
# list(map(st, attrs))

# sc = SentenceCollection()
# sc.add(0, ["a", "b", "c"])
# sc.add(1, ["f", "e", "d"])
# sc.items()
