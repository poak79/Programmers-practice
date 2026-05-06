def solution(my, parts):
    res = ""
    for i in range(len(my)):
        s = parts[i][0]
        e = parts[i][1]
        
        res += my[i][s:e+1]
    
    return res