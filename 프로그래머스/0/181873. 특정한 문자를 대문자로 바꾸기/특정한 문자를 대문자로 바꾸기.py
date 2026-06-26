def solution(my, alp):
    res = ''
    for i in my:
        if i == alp:
            res += i.upper()
        else:
            res += i
            
    return res