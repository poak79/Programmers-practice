def solution(my, ind):
    res = ''
    for i in range(len(my)):
        if i not in ind:
            res += my[i]
    
    return res