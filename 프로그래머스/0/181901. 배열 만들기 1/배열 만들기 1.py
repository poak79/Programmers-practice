def solution(n, k):
    res = []
    for i in range(1, n+1):
        if i % k == 0:
            res.append(i)
            
    res.sort()
    return res