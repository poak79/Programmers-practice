def solution(my, m, c):
    res = ""
    for i in range(0, len(my), m):
        res += my[i + c - 1]
    
    return res