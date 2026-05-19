def solution(s):
    res = []
    res += s
    res.sort()
    resu = ""
    for i in res:
        resu += i
    return resu[::-1]