def solution(my):
    res = ''
    for ch in my:
        if ch not in res:
            res += ch
    
    return res