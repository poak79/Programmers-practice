def solution(n):
    res = ""
    for i in range(1, n+1):
        if i%2 != 0:
            res += "수"
        elif i%2 == 0:
            res += "박"
        
    return res