def solution(a, b):
    res1 = int(str(a) + str(b))
    res2 = 2 * a * b
    
    return res1 if res1>res2 else res2