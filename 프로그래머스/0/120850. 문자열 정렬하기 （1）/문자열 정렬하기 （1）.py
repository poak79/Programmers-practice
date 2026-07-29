def solution(my):
    res = []
    for d in my:
        if d.isdigit():
            res.append(int(d))
            
    return sorted(res)