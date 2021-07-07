

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


# root_five: float = 5 ** (1 / 2)
# numer = lambda n: ((1 + root_five) / 2) ** n



def fib(n):
    """Fibonacci number at a given point."""
    return round(numer(n) / root_five)



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

# divisor_count(10)


def is_prime(n):
    if n >= 2:
        half_n = n // 2
        for i in range(2, half_n + 1):
            if n % i == 0:
                return False
        return True
    return True

# for i in range(21): print(i, is_prime(i))