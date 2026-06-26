def solution(strArr):
    res = []
    for i in range(0, len(strArr)):
        if i%2 == 0:
            res.append(strArr[i].lower())
        else:
            res.append(strArr[i].upper())
            
    return res
        