def solution(i, j, k):
    res = 0
    for a in range(i, j+1):
        res += str(a).count(str(k))
            
    return res