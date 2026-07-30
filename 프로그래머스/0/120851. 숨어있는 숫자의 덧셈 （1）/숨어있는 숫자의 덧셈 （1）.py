def solution(my):
    res = 0
    for i in my:
        if i.isdigit():
            res += int(i)
            
    return res