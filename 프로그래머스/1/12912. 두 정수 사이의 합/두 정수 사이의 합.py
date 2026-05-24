def solution(a, b):
    res = 0
    if a < b:
        for i in range(a, b+1):
            res += i
    elif a > b:
        for i in range(b, a+1):
            res += i
    else:
        res += a
    return res