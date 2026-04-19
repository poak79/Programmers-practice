def solution(a, b):
    res1 = int(str(a) + str(b))
    res2 = int(str(b) + str(a))
    
    if res2 > res1:
        return res2
    else:
        return res1