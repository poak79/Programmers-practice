def solution(my, s, e):
    res = ""
    res += my[:s]
    res += my[s:e+1][::-1]
    res += my[e+1:]
    
    return res