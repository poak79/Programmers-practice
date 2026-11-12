def solution(a, b):
    res = 0
    for i in range(0, len(a)):
        res += a[i]*b[i]
        
    return res