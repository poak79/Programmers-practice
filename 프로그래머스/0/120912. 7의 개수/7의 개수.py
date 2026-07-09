def solution(array):
    res = 0
    for i in array:
        for j in str(i):
            if j == '7':
                res += 1
            
    return res
        