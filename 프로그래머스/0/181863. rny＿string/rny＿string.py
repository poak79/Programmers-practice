def solution(rny):
    res = ''
    for i in range(0, len(rny)):
        if rny[i] == 'm':
            res += "rn"
        else:
            res += rny[i]
        
    return res