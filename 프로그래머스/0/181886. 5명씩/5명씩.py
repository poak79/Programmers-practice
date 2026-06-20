def solution(names):
    res = []
    for i in range(0, len(names)):
        if i%5 == 0:
            res.append(names[i])
            
    return res