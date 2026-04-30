def solution(num):
    res = ""
    for i in range(1, len(num)):
        diff = num[i] - num[i-1]
        
        if diff == 1:
            res += "w"
        elif diff == -1:
            res += "s"
        elif diff == 10:
            res += "d"
        elif diff == -10:
            res += "a"
        
    return res