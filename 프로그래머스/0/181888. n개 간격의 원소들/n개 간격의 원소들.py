def solution(num, n):
    res = []
    for i in range(0, len(num)):
        if i%n == 0:
            res.append(num[i])
            
    return res