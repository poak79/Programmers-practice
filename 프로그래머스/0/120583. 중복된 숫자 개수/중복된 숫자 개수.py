def solution(array, n):
    res = 0
    for i in array:
        if i == n:
            res += 1
            
    return res