def solution(n):
    res = []
    for i in range(1, n+1):
        if i%2 != 0:
            res.append(i)
            
    return res