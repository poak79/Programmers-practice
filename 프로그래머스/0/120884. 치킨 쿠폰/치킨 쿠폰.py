def solution(chicken):
    res = 0
    c = chicken
    while c >= 10:
        s = c // 10
        res += s
        c = c % 10 + s
        
    return res