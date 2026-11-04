def solution(x, n):
    res = []
    a = x
    for _ in range(n):
        res.append(x)
        x += a
        
    return res