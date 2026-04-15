def solution(a, b):
    res = ''

    for i in range(len(a)):
        res += a[i]
        res += b[i]
    
    return res