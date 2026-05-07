def solution(my):
    res = []
    res.append(my)
    for i in range(len(my)-1):
        res.append(my[i+1:])
        
    res.sort()
    return res