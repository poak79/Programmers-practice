def solution(num):
    if len(num) >= 11:
        res = 0
        for i in num:
            res += i
    else:
        res = 1
        for i in num:
            res *= i
    
    return res