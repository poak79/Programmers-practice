def solution(num):
    res = ""
    for i in range(0, len(num)-4):
        res += '*'
        
    res += num[-4:]
    return res