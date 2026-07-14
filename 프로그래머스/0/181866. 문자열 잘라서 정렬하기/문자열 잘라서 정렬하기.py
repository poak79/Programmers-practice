def solution(my):
    res = [w for w in my.split('x') if w]
    res.sort()
    return res