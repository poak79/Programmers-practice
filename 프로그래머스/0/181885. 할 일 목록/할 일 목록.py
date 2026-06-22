def solution(todo, fin):
    res = []
    for i in range(0, len(fin)):
        if fin[i] == False:
            res.append(todo[i])
            
    return res