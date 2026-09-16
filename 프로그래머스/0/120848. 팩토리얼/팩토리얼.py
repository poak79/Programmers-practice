def solution(n):
    i, fact = 1, 1
    while fact * (i+1) <= n:
        i += 1
        fact *= i
        
    return i