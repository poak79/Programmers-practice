def solution(n):
    res = []
    res.append(n)
    while n != 1:
        if n%2 == 0:
            res.append(n/2)
            n /= 2
        else:
            res.append(3*n+1)
            n = 3*n+1
    
    return res