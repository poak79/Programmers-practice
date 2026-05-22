def solution(n):
    res = []
    for i in str(n):
        res.append(int(i))
        
    return res[::-1]