def solution(a, d, included):
    res = 0
    for i in range(len(included)):
        if included[i]:
            res += a + d * i
    return res        
    