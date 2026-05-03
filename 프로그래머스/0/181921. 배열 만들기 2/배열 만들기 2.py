def solution(l, r):
    res = []
    for i in range(l, r+1):
        if set(str(i)) <= {"0", "5"}:
            res.append(i)
        
    return res if res else [-1]