def solution(s):
    res = ""
    if len(s)%2 == 0:
        res += s[len(s)//2-1]
        res += s[len(s)//2]
        return res
    else:
        return s[len(s)//2]