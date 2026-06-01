def solution(n, numlist):
    res = []
    for i in numlist:
        if i%n == 0:
            res.append(i)
    
    return res