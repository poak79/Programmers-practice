def solution(my, pat):
    res = 0
    
    for i in range(len(my) - len(pat) + 1):
        if my[i:i+len(pat)] == pat:
            res += 1
            
    return res
        