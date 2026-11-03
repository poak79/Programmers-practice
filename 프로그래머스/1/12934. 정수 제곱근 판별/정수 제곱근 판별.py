import math

def solution(n):
    if n >= 0 and math.isqrt(n) ** 2 == n:
        return (math.isqrt(n)+1) ** 2
    else:
        return -1