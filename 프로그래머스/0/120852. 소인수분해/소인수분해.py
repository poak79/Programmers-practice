def solution(n):
    i = 2
    res = []
    while i * i <= n:
        if n % i != 0:
            i += 1
        else:
            n //= i
            res.append(i)
            
    if n > 1:
        res.append(n)
    
    
    return list(dict.fromkeys(res))